const superagent = require("superagent");
const cheerio = require("cheerio");
const fs = require("fs");

const mainUrl = "https://weibo.com/2656274875/LgWUkqJqX?refer_flag=1001030103_";

let getData = (url) => {
  superagent.get(mainUrl).end((err, res) => {
    if (err) {
      throw Error(err);
      return;
    }
    // 解析数据cheerio
    // let $ = cheerio.load(res.text, { decodeEntities: false });
    let $ = cheerio.load(res.text);
    let data = [];
    const listtimes = $(".vue-recycle-scroller__item-view");
    listtimes.each(function (index, d) {
      // const context = $(d).children()[0]
      console.log(index);
    });
    // const listItems = $("span");
    // $('span').each(function (index, d) {
    //   const children = $($(d).children()[0])
    //   console.log(children);
    //   console.log(index,$(d).text())
    // });
  });
  console.log("return");
};

getData(mainUrl);
