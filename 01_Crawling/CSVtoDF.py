import os
import pandas as pd

def SearchCSV():
    """
    현재 경로 안의 csv 파일을 모두 찾아 파일명을 기준(news/comment)으로\n
    뉴스기사와 댓글 파일을 구분하여 각각의 리스트에 담아 반환합니다.
    """

    filelist = os.listdir('./')
    newsCSV = []
    commentCSV = []

    for file in filelist:

        if '.csv' in file:
            
            if 'news' in file:
                newsCSV.append(os.path.abspath(file))

            if 'comment' in file:
                commentCSV.append(os.path.abspath(file))
                
    return newsCSV, commentCSV

def CSVtoDF(file_list : list):
    """
    SearchCSV 함수로 찾은 뉴스기사와 댓글 파일 리스트를 각각 이 함수에 넣으면,\n
    파일명을 기준(news/comment)으로 뉴스기사와 댓글 파일을 구분하여 데이터프레임을 만들고 반환합니다.\n
    
    CSVtoDF(SearchCSV()[0])이 뉴스기사 데이터프레임,\n
    CSVtoDF(SearchCSV()[1])이 댓글 데이터프레임입니다.
    """

    df = pd.DataFrame()

    for file in file_list:

        if 'news' in file:
            news_df = pd.read_csv(file)
            news_df = news_df[['MainCategory', 'SubCategory', 'WritedAt', 'Title', 'Content', 'URL', 'PhotoURL', 'Writer', 'Press', 'Stickers']]
            
            df = news_df

        if 'comment' in file:
            
            comments_df = pd.read_csv(file)
            comments_df.rename(columns = {'Url':'URL'}, inplace=True)
            comments_df = comments_df[['URL', 'UserID', 'UserName', 'WritedAt', 'Content']]
                
            df = comments_df
            
        return df