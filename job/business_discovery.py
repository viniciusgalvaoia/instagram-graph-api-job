from ig_helpers import build_url, request_data


# Account id, followers_count, media_count
def get_followers_and_media_count(base, username, node, access_token):
    parameters = (
        f"?fields=business_discovery.username({username}){{followers_count,media_count}}"
        f"&access_token={access_token} "
    )
    url = build_url(base, node, parameters)
    return request_data(url)


# M edia id, comments_count, like_count
def get_basic_media_metrics(base, username, node, access_token):
    parameters = (
        f"?fields=business_discovery.username({username}){{followers_count,media_count,media{{"
        f"comments_count,like_count}}}}&access_token={access_token} "
    )
    url = build_url(base, node, parameters)
    return request_data(url)
