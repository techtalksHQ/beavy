from beavy.common.rate_limits import rate_limit
from beavy.app import cache
from beavy.utils import api_only

from .lib import extract_oembed, extract_info
from .blueprint import blueprint


from flask import request

@blueprint.route('extract')
@cache.memoize(15 * 60) # keep in cache for 15min
# @login_required
@rate_limit("1/second")
@api_only
def extract():
    url = request.args["url"]
    result = {"url": url,
              "info": extract_info(url)}
    if request.args.get("oembed", False):
        result["oembed"] = extract_oembed(url)
    return result
