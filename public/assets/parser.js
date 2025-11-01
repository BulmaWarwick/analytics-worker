const { parse } = require('node-html-parser');
const { URL } = require('url');

const parsePage = async (url) => {
  const parsedUrl = new URL(url);
  if (!parsedUrl.protocol ||!parsedUrl.host) {
    throw new Error('Invalid URL');
  }

  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}: ${response.status} ${response.statusText}`);
  }

  const html = await response.text();
  const dom = parse(html);
  return dom;
};

module.exports = { parsePage };