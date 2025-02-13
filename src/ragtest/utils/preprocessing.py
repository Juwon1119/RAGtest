import pickle
from pathlib import Path

import polars as pl

from ragtest.path import PKL_PATH


def read_raw_data(pkl_path: Path = PKL_PATH) -> pl.DataFrame:
    with open(pkl_path, 'rb') as file:
        data = pickle.load(file)
    return pl.DataFrame({"query": list(data.keys()), "answer": list(data.values())})

def remove_unnecessary_answer_parts(df : pl.DataFrame) -> pl.DataFrame:
    #답변에서 반복되는 pattern"
    pattern = r"위 도움말이 도움이 되었나요\?[\s\S]*?별점[1-5]점[\s\S]*?소중한 의견을 남겨주시면 보완하도록 노력하겠습니다\.[\s\S]*?보내기"
    return df.with_columns(pl.col("answer").str.replace(pattern, "", literal=False))
