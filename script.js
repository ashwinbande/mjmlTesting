// show local url in gmail
(()=>{let e;for(;e=document.evaluate("//img[contains(@src, 'googleusercontent.com')][contains(@src, '#')]",document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue;){let t=e.attributes.src.value;t=t.substr(t.indexOf("#")+1),e.attributes.src.value=t}})();
