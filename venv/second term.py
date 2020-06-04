from headers import website_target

import pandas as pd
import numpy as np

website_target('https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_keyword&from_keyword_history=false&search%5Bkeywords%5D=kopi+specialty')

website_target("https://www.bukalapak.com/products?utf8=%E2%9C%93&search%5Bkeywords%5D=kopi+specialty&search%5Bsort_by%5D=last_relist_at%3Adesc")

website_target("https://www.bukalapak.com/products?utf8=%E2%9C%93&search%5Bkeywords%5D=kopi+specialty&search%5Bsort_by%5D=weekly_sales_ratio%3Adesc")
print('*'*100)
