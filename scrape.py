import instagram_scraper as ig
import sys

TERM = "dankmemes"

sys.argv.append(TERM)
sys.argv.append("--tag")

sys.argv.append("--media-types")
sys.argv.append("image")

print ("Beginning to scrape #{}...".format(TERM))

ig.main()
