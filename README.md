# patent-extractor

Author: Riki Akbar (github.com/akbarriki)

This is the repository of patent-extractor, a piece of python code to extract Patents from <a href="patents.google.com">Google Patents</a>. Currently, the scope of tool is limited to patents in Chinese and English only.

To run the extraction, type the following command in your terminal/command prompt. Please specify the list of patent ids to extract and the target directory in which the patent texts are stored.


```
# python patents.py [LIST_OF_PATENT_IDS] [TARGET_DIRECTORY]
python patents.py "patent_num.txt" "target"
```

To avoid the scraping process getting aborted due to the long list of patent ids in patent_num.txt, we put a 5-minute delay for every 800 patent ids. 

So, the result will look like this:
```
loading CN1886949A...complete (status:Ok)
loading CN1241948A...complete (status:Ok)
loading CN1732724A...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
loading WO1998028023A1...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
*** Delay 300 s***
loading US6167455A...complete (status:Ok)
loading US5600768A...complete (status:Ok)
loading US5537529A...complete (status:Ok)
```

feedbacks are welcome!

