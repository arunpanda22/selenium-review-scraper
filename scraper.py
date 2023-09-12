import asyncio
from pyppeteer import launch

async def scrape_amazon_reviews(i):
    try:
        browser = await launch(headless=False, defaultViewport=None)
        page = await browser.newPage()
        url = f'https://www.amazon.in/product-reviews/B09RG9WPTC/ref=cm_cr_getr_d_paging_btm_next_4?pageNumber={i}'
        await page.goto(url)

        await page.waitForSelector('div[data-hook="review"]', timeout=5000)  # Wait for reviews to load

        reviewElements = await page.querySelectorAll('div[data-hook="review"]')
        reviews = []

        for element in reviewElements:
            reviewText = await page.evaluate('(el) => el.textContent.trim()', element)
            reviews.append({'reviewText': reviewText})

        return reviews

    except Exception as e:
        print("Error:", e)
    finally:
        await browser.close()

async def main():
    reviews = []

    for i in range(1, 6):
        reviews_batch = await scrape_amazon_reviews(i)
        reviews.extend(reviews_batch)

    print('Scraped reviews:', reviews)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
