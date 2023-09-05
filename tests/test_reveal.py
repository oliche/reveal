from reveal.api import RevealSite
import pandas as pd
from pathlib import Path
import webbrowser
import numpy as np

ASSETS_PATH = Path(__file__).parent / "assets"

def test_basic():
    lu_path = ASSETS_PATH / "left_upper.png"
    ru_path = ASSETS_PATH / "right_upper.png"
    ll_path = ASSETS_PATH / "left_lower.png"
    rl_path = ASSETS_PATH / "right_lower.png"

    arr = np.empty((2,2), object)

    arr[0, 0] = {"image_path": lu_path, "title": "Left Upper"}
    arr[0, 1] = {"image_path": ru_path, "title": "Right Upper"}
    arr[1, 0] = {"image_path": ll_path, "title": "Left Lower"}
    arr[1, 1] = {"image_path": rl_path, "title": "Right Lower"}
    
    df = pd.DataFrame(arr)

    rs = RevealSite(df, "basic_test")
    rs.build()

    webbrowser.open(f"file://{rs.reveal_path}/basic_test.html")

def test_basic_compare():
    lu_path = ASSETS_PATH / "left_upper.png"
    ru_path = ASSETS_PATH / "right_upper.png"
    ll_path = ASSETS_PATH / "left_lower.png"
    rl_path = ASSETS_PATH / "right_lower.png"

    lu_path_cmp = ASSETS_PATH / "left_upper_compare.png"
    ru_path_cmp = ASSETS_PATH / "right_upper_compare.png"
    ll_path_cmp = ASSETS_PATH / "left_lower_compare.png"
    rl_path_cmp = ASSETS_PATH / "right_lower_compare.png"

    arr = np.empty((2,2), object)

    arr[0, 0] = {"image_path": lu_path,
                 "image_path_compare": lu_path_cmp, 
                 "title": "Left Upper",}
    arr[0, 1] = {"image_path": ru_path, 
                 "image_path_compare": ru_path_cmp, 
                 "title": "Right Upper"}
    arr[1, 0] = {"image_path": ll_path,
                 "image_path_compare": ll_path_cmp, 
                 "title": "Left Lower"}
    arr[1, 1] = {"image_path": rl_path,
                 "image_path_compare": rl_path_cmp, 
                 "title": "Right Lower"}
    
    df = pd.DataFrame(arr)

    rs = RevealSite(df, "basic_test_slider")
    rs.build()

    webbrowser.open(f"file://{rs.reveal_path}/basic_test_slider.html")



