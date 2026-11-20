import streamlit as st
from lotto_utils import *

"""st.title('🎱로또번호생성기')
n = st.number_input('몇게임할까요?', min_value=1, max_value=10, value=5)

if st.button('번호뽑기'):
    st.session_state.games = make_games(n)

    games = make_games(n)
    lines=[]
    for i in range(n):
        lines.append(f'**{i+1:2d}게임** : {to_text(games[i])}')
    st.code('\n'.join(lines), language=None)

if 'games' in st.session_state:
    for i in range(len(st.session_state.games)):
        st.write(f'**{i+1:2d}게임** : {to_text(st.session_state.games[i])}')
"""
st.title('🎱로또번호생성기')

@st.cache_data
def get_counts():
    return load_counts('lotto.csv')

count = get_counts()
tab1, tab2, tab3 = st.tabs(['🎲자동뽑기', '📊번호별통계', '✋수동선택'])

with tab1:
    n = st.number_input('몇게임할까요?', min_value=1, max_value=10, value=5)
    col1, col2 = st.columns(2)
    if col1.button('랜덤으로뽑기'):
        st.session_state.games= make_games(n)
    if col2.button('자주나온번호로뽑기'):
        games = []
        for i in range(n):
            games.append(make_hot_game(count))
        st.session_state.games= games
if 'games' in st.session_state:
    for i in range(len(st.session_state.games)):
        st.write(f'**{i+ 1}게임** : {to_text(st.session_state.games[i])}')

with tab2:
    st.write('1회~ 1250회당첨번호6개기준(보너스제외)')
    st.bar_chart(pd.Series(count, name='당첨횟수'))
    top10 = top_numbers(count, 10)
    st.write('자주나온번호TOP 10 :', to_text(top10))

