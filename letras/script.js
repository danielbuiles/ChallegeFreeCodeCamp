const puppeteer = require('puppeteer');

async function getSong(name) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(`https://www.musixmatch.com/es/search/${name}`);
  await page.waitForTimeout(1000);

  const url = await page.evaluate(() => {
    const artist = document.querySelector('#search-all-results .media-card-title a').href;
    return artist;
  });

  await page.goto(url);
  await page.waitForSelector('.mxm-lyrics .lyrics-to').textContent;

  const lyrics = await page.evaluate(() => {
        const lyrics1 = document.querySelector('.mxm-lyrics .mxm-lyrics__content .lyrics__content__ok').innerText;
        const lyrics2 = document.querySelector('.mxm-lyrics span div p span').innerText;
        return lyrics1+lyrics2;
    });

    console.log(lyrics);

  await browser.close();
}

getSong('21 guns');