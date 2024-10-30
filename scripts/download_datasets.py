# downloads the zstd compressed datasets from the google drive

import concurrent
import gdown

part_ids = [ 
    '1PFoKOPJA_WSt4b3w_6PkGt2GRM02QYgc',
    '11nQacibpIphoxuyoRW4NU0AD-a4Eb4xM',
    '18e5uROegtMLySFpbAm1l9ZazDahrWR2-',
    '1CZpiY_rKWeHKapWnrZOlNKp58WsLfke2',
    '1W9GYYbqQOkImBaAju3dbQnhEq01YVMc3',
    '1XbrQJBKBH04bFNXw2kcj_L-ePv9uAXEH',
    '1F4w2h5t65egvNL-z38cXs27G_-CQ4J1c',
    '1Q2RD6i7QnbSHMu2WkuEJfCqjmOELCwIn',
    '1IS4hguKyWINqfuEoRh_JxVWiSD5rrzOj'
]

output_folder='tmp'
name = '682_proj_datasets.tar.zst'

def download_file(part_id, index):
    output_file_name = f'{output_folder}/{name}.tar.zst.part_{index:02d}'
    gdown.download(id=part_id, output=output_file_name, quiet=False)

def download_datasets():
  # We can use a with statement to ensure threads are cleaned up promptly
  with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
      # Start the load operations and mark each future with its URL
      future_to_url = {executor.submit(download_file, id, idx): (idx,id) for idx, id in enumerate(part_ids)}
      for future in concurrent.futures.as_completed(future_to_url):
          url = future_to_url[future]
          try:
              data = future.result()
          except Exception as exc:
              print('%r generated an exception: %s' % (url, exc))
          else:
              print('%r page is %d bytes' % (url, len(data)))

download_datasets()
