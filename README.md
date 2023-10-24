# patent-extractor

Author: Riki Akbar (github.com/akbarriki)

This is the repository of patent-extractor, a piece of python code to extract Patents from <a href="patents.google.com">Google Patents</a>. Currently, the scope of tool is limited to patents in Chinese and English only.

To run the extraction, type the following command in your terminal/command prompt. Please specify the list of patent ids to extract and the target directory in which the patent texts are stored.


```
# python patents.py [LIST_OF_PATENT_IDS] [TARGET_DIRECTORY]
python patents.py "patent_num.txt" "target/"
```

Result:
```
loading CN1886949A...complete (status:Ok)
loading CN1241948A...complete (status:Ok)
loading CN1732724A...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
loading WO1998028023A1...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
loading WO2005062560A1...complete (status:Ok)
```

feedbacks are welcome!

