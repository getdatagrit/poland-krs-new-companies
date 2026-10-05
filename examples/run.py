# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/poland-krs-new-companies").call(run_input={
    "mode": "newRegistrations",
    "daysBack": 2,
    "scanDepth": "recent",
    "maxItems": 30
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
