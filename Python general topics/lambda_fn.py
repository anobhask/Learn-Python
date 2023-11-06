## Lambda Functions

m_multiply = lambda number : number * number

m_list = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
m_list = range(0, 10)
print(list(m_list))
map_res = map(m_multiply, m_list)
print(map_res)
map_res = filter(m_multiply, m_list)
print(map_res)

print(list(map_res))

map_res = map(lambda x : x % 2 == 0, m_list)
print(map_res)
print(list(map_res))

map_res = filter(lambda x : x % 2 == 0, m_list)
print(map_res)
print(list(map_res))