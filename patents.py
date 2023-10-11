import pandas as pd
import requests, warnings, sys
from bs4 import BeautifulSoup as bs
warnings.filterwarnings("ignore")

class Patents():
  def __init__(self, patent_src_file=sys.argv[1], patent_tgt_dir=sys.argv[2]):
    self.patent_tgt_dir = patent_tgt_dir
    self.patent_src_file = patent_src_file
    with open(self.patent_src_file, "r") as fr:
      self.patent_ids = [line.strip() for line in fr.readlines()]
  
  def get_patent_tgt_dir(self):
    return self.patent_tgt_dir
  
  def get_patent_src_file(self):
    return self.patent_src_file

  def get_patent_text(self, patent_id:str):

    lang_ = "en" if patent_id[:2] in ("WO","US") else "zh"
    url = f"https://patents.google.com/patent/{patent_id}/{lang_}"

    resp = requests.get(url)    
    if resp.ok:
      try:
        soup = bs(resp.content, 'html.parser')
        title = soup.title.get_text().split("-")[1].strip()
        abstract = soup.find("div",{"class":"abstract"}).get_text().strip()
        description = soup.find("section",{"itemprop":"description"}).get_text().strip()
        claims = soup.find("section",{"itemprop":"claims"}).get_text().strip()

        content_ = f"{title}\n\n{abstract}\n\n{description}\n\n{claims}"

        with open(f"{self.patent_tgt_dir}{patent_id}_{title}.txt","w", encoding="utf-8") as fw:
            fw.write(content_)
        return 1
      except:
        return 0
    
  def get_patent_bulk(self):
    for patent_id in self.patent_ids:
      print(f"loading {patent_id}...", end="")
      status = "Ok" if self.get_patent_text(patent_id) else "Not Ok"
      print(f"complete (status:{status})")


if __name__ == "__main__":
  source_file = "patent_num.txt"
  target_dir = "target/"
  patents = Patents(source_file, target_dir)
  patents.get_patent_bulk()
#   print(patents.get_patent_text("WO2005062560A1"))