#!/user/bin/python
#-*- coding: UTF-8 -*-

import random as rd

'''
[
[1,2,3,4],
[2,2,3,4],
[3,2,3,4],
[4,2,3,4],
]

[
[1,1,2,2],
[0,4,0,4],
[3,2,3,4],
[4,2,3,4],
]

┌─┬─┬─┬─┐
│1│2│3│4│
├─┼─┼─┼─┤
│2│2│3│4│
├─┼─┼─┼─┤
│3│2│3│4│
├─┼─┼─┼─┤
│4│2│3│4│
└─┴─┴─┴─┘
'''

class Matrix(object):
    def __init__(self):
        self.init_matrix()
        self.spawn_numbers(100)
    '''
    list_push(tempList):
        将一个长度为4的列表按规则压缩
        [0202] -> [4000]
        [0424] -> [4240]
        [2248] -> [4480]
        
    spawn_numbers:
        在数字为0的地方生成2或4或8
        
    print_matrix:
        以整齐格式打印出当前矩阵
        
    init_matrix:
        将self.matrix初始化为4*4的0矩阵
        
    __ret_line_in_string(line):
        将matrix[line]列表使用制表符包装，返回一个字符串
        
    __get_max_length:
        为了制表符包装整齐，获取所有最长元素的长度，返回self.mx
        

    '''
    #def dectect_death(self):

    def move(self):
        inp = input('input w/a/s/d')
        if   inp == 'w':
            self.__move('up')
        elif inp == 'a':
            self.__move('left')
        elif inp == 's':
            self.__move('down')
        elif inp == 'd':
            self.__move('right')

    def list_push(self,tempList):
        #去掉所有的0
        while True:
            if 0 in tempList:
                tempList.remove(0)
            else:break
        #补长
        tempList += [0]*(4-len(tempList))
        #压缩
        for i in range(3):
            if tempList[i] == tempList[i+1]:
                tempList.pop(i)
                tempList.append(0)
                tempList[i] = tempList[i]*2
        return tempList
                
    
    def spawn_numbers(self,coin=40):
        if rd.randint(1,100) <= coin:
            while True:
                x = rd.randint(0,3)
                y = rd.randint(0,3)
                if self.matrix[x][y] == 0:
                    self.matrix[x][y] = rd.choice([2,2,4,8])
                    break

    def print_matrix(self):
        self.__get_max_length()
        string = []
        string.append('┌{0}┬{0}┬{0}┬{0}┐'.format('─'*self.mx))
        string.append(self.__ret_line_in_string(0))
        string.append('├{0}┼{0}┼{0}┼{0}┤'.format('─'*self.mx))
        string.append(self.__ret_line_in_string(1))
        string.append('├{0}┼{0}┼{0}┼{0}┤'.format('─'*self.mx))
        string.append(self.__ret_line_in_string(2))
        string.append('├{0}┼{0}┼{0}┼{0}┤'.format('─'*self.mx))
        string.append(self.__ret_line_in_string(3))
        string.append('└{0}┴{0}┴{0}┴{0}┘'.format('─'*self.mx))
        for i in string:
            print(i)

    def init_matrix(self):
        self.matrix = []
        for i in range(4):self.matrix.append([0]*4)
        return self.matrix

    def __ret_line_in_string(self,line):
        l = '│'
        for i in self.matrix[line]:
            if i == 0:i=" "
            i = ' '*(self.mx-len(str(i))) + str(i)
            l = l + i + '│'
        return l

    def __get_max_length(self):
        self.mx = 1
        for i in self.matrix:
            for j in i:
                if len(str(j))>1:self.mx = len(str(j))
        return self.mx

    def __move(self,direction):
        self.__newM = []
        #UP
        if   direction == 'up':
            self.__a = []
            for i in [0,1,2,3]:
                self.__b = []
                for j in [0,1,2,3]:
                    self.__b.append(self.matrix[j][i])
                self.__a.append(self.__b)
            self.__b = []
            for i in self.__a:
                i = self.list_push(i)
                self.__b.append(i)
            for i in [0,1,2,3]:
                self.__a = []
                for j in [0,1,2,3]:
                    self.__a.append(self.__b[j][i])
                self.__newM.append(self.__a)
        #LEFT
        elif direction == 'left':
            for i in self.matrix:
                i = self.list_push(i)
                self.__newM.append(i)
        #DOWN
        elif direction == 'down':
            self.__a = []
            for i in [0,1,2,3]:
                self.__b = []
                for j in [3,2,1,0]:
                    self.__b.append(self.matrix[j][i])
                self.__a.append(self.__b)
            self.__b = []
            for i in self.__a:
                i = self.list_push(i)
                self.__b.append(i)
            for i in [3,2,1,0]:
                self.__a = []
                for j in [0,1,2,3]:
                    self.__a.append(self.__b[j][i])
                self.__newM.append(self.__a)
        #RIGHT
        elif direction == 'right':
            for i in self.matrix:
                i.reverse()
                i = self.list_push(i)
                i.reverse()
                self.__newM.append(i)
        #RETURN
        self.matrix = self.__newM
        return 'OK'

def Main():
    m = Matrix()
    while True:
        m.print_matrix()
        m.move()
        m.spawn_numbers()

if __name__ == '__Main__':
    Main()


'''
数字生成还不够智能
居然可以原地不动等数字生成？？有瑕疵
'''

