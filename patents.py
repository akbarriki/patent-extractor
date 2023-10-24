import pandas as pd
import requests, warnings, sys, time
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

    lang_ = "zh" if patent_id[:2] == "CH" else "en"
    url = f"https://patents.google.com/patent/{patent_id}/{lang_}"

    resp = requests.get(url)    
    if resp.ok:
      try:
        soup = bs(resp.content, 'html.parser')
        content_ = ""
        
        try:
          content_ += soup.title.get_text().split("-")[1].strip() + "\n\n"
        except:
          pass

        try:
          content_ += soup.find("div",{"class":"abstract"}).get_text().strip() + "\n\n"
        except:
          pass
        
        try:
          content_ += soup.find("section",{"itemprop":"description"}).get_text().strip() + "\n\n"
        except:
          pass

        try:
          content_ += soup.find("section",{"itemprop":"claims"}).get_text().strip()
        except:
          pass

        with open(f"{self.patent_tgt_dir}/{patent_id}.txt","w", encoding="utf-8") as fw:
            fw.write(content_)
        return 1
      except:
        print(self.patent_tgt_dir)
        print(patent_id)
        print(resp.status_code)
        return 0
    
  def get_patent_bulk(self):
    delay = 300
    for i, patent_id in enumerate(self.patent_ids):
      if i > 0  and i % 800 == 0:
        time.sleep(delay)
        print(f"*** Delay {delay} s***")
      print(f"loading {patent_id}...", end="")
      status = "Ok" if self.get_patent_text(patent_id) else "Not Ok"
      if status == "Not Ok":
        break
      print(f"complete (status:{status})")


if __name__ == "__main__":
#   source_file = "patent_num.txt"
#   target_dir = "target"
  patents = Patents()
  patents.get_patent_bulk()
#   print(patents.get_patent_text("WO2005062560A1"))