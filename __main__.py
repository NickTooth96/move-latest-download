import os
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate


dp = download_path.find()
mr = most_recent.find(dp)
relocate.move(mr,dp,os.getcwd())
# relocate.undo_last_move()
