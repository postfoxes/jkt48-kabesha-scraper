import os
import asyncio
import httpx
from curl_cffi import requests
from bs4 import BeautifulSoup

def get_kabesha_urls():
    """Mengambil semua URL foto member dari halaman list JKT48."""
    print("Sedang mengambil daftar member...")
    url_list = "https://jkt48.com/member/list?lang=id"
    
    # Menggunakan curl_cffi untuk bypass proteksi bot (impersonate chrome)
    response = requests.get(url_list, impersonate="chrome101")
    soup = BeautifulSoup(response.content, 'html.parser')

    divs = soup.find_all('div', class_="entry-member")
    
    base_url = 'https://jkt48.com'
    urls = []
    
    for tag in divs:
        img_tag = tag.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_path = img_tag['src']
            # Bersihkan URL jika ada double slash
            full_url = f"{base_url}{img_path}" if img_path.startswith('/') else f"{base_url}/{img_path}"
            urls.append(full_url)
    
    print(f"Ditemukan {len(urls)} member.")
    return urls

async def download_all_images(urls, folder):
    """Mengunduh semua gambar secara asinkron."""
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Folder '{folder}' dibuat.")

    # Membatasi jumlah koneksi simultan agar tidak diblokir
    semaphore = asyncio.Semaphore(10)

    async def download_image(client, url):
        async with semaphore:
            try:
                # Mengambil nama dari URL (misal: abigail_rachel)
                member_name = url.split('/')[-1].split('.')[0]
                filename = f"member_{member_name}.jpg"
                filepath = os.path.join(folder, filename)

                response = await client.get(url, timeout=15.0)
                if response.status_code == 200:
                    with open(filepath, 'wb') as f:
                        f.write(response.content)
                    print(f"✅ Berhasil: {member_name}")
                else:
                    print(f"❌ Gagal ({response.status_code}): {member_name}")
            except Exception as e:
                print(f"⚠️ Error pada {url}: {str(e)}")

    print(f"Memulai proses download ke folder '{folder}'...")
    async with httpx.AsyncClient() as client:
        tasks = [download_image(client, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    # 1. Ambil list URL
    urls = get_kabesha_urls()
    
    # 2. Jalankan download secara async
    if urls:
        output_dir = "jkt48_kabeshas"
        asyncio.run(download_all_images(urls, output_dir))
        print("\n--- Semua tugas selesai ---")
    else:
        print("Gagal mengambil daftar URL. Pastikan koneksi internet lancar.")