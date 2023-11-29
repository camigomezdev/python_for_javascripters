function getUrlConf(host) {
    switch (host) {
        case "www.example-a.dev":
            return "firstApp.urls"
        case "www-example-b.dev":
            return "secondApp.urls"
        case "www.example-c.dev":
            return "thirdApp.urls"
        default:
            return "Sorry, no match"
    }
}

console.log(getUrlConf("www.example-a.dev"))
// firstApp.urls

console.log(getUrlConf("www.example.dev"))
// Sorry, no match
