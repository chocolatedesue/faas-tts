

def download_with_tqdm(url,detination):
    assert url and detination
    import requests
    from tqdm import tqdm
    from loguru import logger
    try:
        content_length = int(requests.head(url).headers['Content-Length'])
        r = requests.get(url, stream=True)
        with open(detination, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(1024), total=content_length / 1024, unit='KB'):
                f.write(data)
    except KeyError as e:
        logger.error(e)
        r = requests.get(url)
        with open(detination, 'wb') as f:
            f.write(r.content)
    except Exception as e:
        logger.error(e)
        raise e 
