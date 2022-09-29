library(rvest)
listing_url <- "https://subslikescript.com/series/Bluey-7678620"
res <- read_html(listing_url)
html <- htmlParse(res)
links <- xpathSApply(html, path = "//a", xmlGetAttr,"href")
ep_links <- paste0("https://subslikescript.com", links[grepl("series/Bluey", links)])

pg <- read_html(ep_links[1])
