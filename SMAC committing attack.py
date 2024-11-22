
# S-Box for SubBytes step  
sbox = [  
    # 0     1      2     3     4     5     6     7     8    9     A     B     C      D     E     F  
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],  
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],  
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],  
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],  
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],  
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],  
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],  
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],  
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],  
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],  
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],  
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],  
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],  
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],  
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],  
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0F, 0xb0, 0x54, 0xbb, 0x16],  
]

inverse_sbox = [
    [0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb],
    [0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb],
    [0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e],
    [0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25],
    [0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92],
    [0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84],
    [0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06],
    [0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b],
    [0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73],
    [0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e],
    [0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b],
    [0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4],
    [0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f],
    [0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef],
    [0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61],
    [0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d]
    ]
# def flatten_with_comprehension(two_d_array):  
#     return [item for sublist in two_d_array for item in sublist]

# for i in range(2**8):
#     if i not in flatten_with_comprehension(sbox) :
#         print(i)
        
def sub_bytes(state):  
    return [[sbox[b >> 4][b & 0x0F] for b in row] for row in state]  

def shift_rows(state):  
    return [  
        state[0],  
        state[1][1:] + state[1][:1],  
        state[2][2:] + state[2][:2],  
        state[3][3:] + state[3][:3],  
    ]  

def inverse_shift_rows(state):  
    """ 对 AES 状态执行逆行移位操作 """  
    new_state = [[0] * 4 for _ in range(4)] 
    # 逆行移位  
    new_state[0] = state[0]
    new_state[1] = state[1][-1:] + state[1][:-1]  # 第1行右移1位  
    new_state[2] = state[2][-2:] + state[2][:-2]  # 第2行右移2位  
    new_state[3] = state[3][-3:] + state[3][:-3]  # 第3行右移3位  
    return new_state 

def xtime(x):  
    """ 计算 x*2 在 GF(2^8) 中 """  
    if x & 0x80:  # 如果最高位为1  
        return ((x << 1) ^ 0x1b) & 0xff  # 异或多项式 x^8 + x^4 + x^3 + x + 1  
    else:  
        return (x << 1) & 0xff  # 否则只是左移  

def mix_columns(state):  
    """ 对 AES 状态执行 MixColumns 操作 """  
    # 创建一个新的状态矩阵  
    new_state = [[0] * 4 for _ in range(4)]  
    
    for j in range(4):  # 对每列进行处理  
        # 提取当前列  
        a = [state[i][j] for i in range(4)]  # 列向量  
        
        # MixColumns 过程  
        new_state[0][j] = xtime(a[0]) ^ xtime(a[1]) ^ a[1] ^ a[2] ^ a[3]  
        new_state[1][j] = a[0] ^ xtime(a[1]) ^ xtime(a[2]) ^ a[2] ^ a[3]  
        new_state[2][j] = a[0] ^ a[1] ^ xtime(a[2]) ^ xtime(a[3]) ^ a[3]  
        new_state[3][j] = xtime(a[0]) ^ a[0] ^ a[1] ^ a[2] ^ xtime(a[3])  
    
    return new_state  

def inverse_mix_columns(state):  
    """ 对 AES 状态执行逆列混淆操作 """  
    new_state = [[0] * 4 for _ in range(4)]  
    
    for j in range(4):  # 对每列进行处理  
        a = [state[i][j] for i in range(4)]  # 列向量  
        new_state[0][j] = (xtime(xtime(xtime(a[0]))) ^ xtime(xtime(a[0])) ^ xtime(a[0]) ^ 
                           xtime(xtime(xtime(a[1]))) ^                      xtime(a[1]) ^ a[1] ^ 
                           xtime(xtime(xtime(a[2]))) ^ xtime(xtime(a[2])) ^               a[2] ^ 
                           xtime(xtime(xtime(a[3]))) ^                                    a[3])  
        
        new_state[1][j] = (xtime(xtime(xtime(a[1]))) ^ xtime(xtime(a[1])) ^ xtime(a[1]) ^ 
                           xtime(xtime(xtime(a[2]))) ^                      xtime(a[2]) ^ a[2] ^ 
                           xtime(xtime(xtime(a[3]))) ^ xtime(xtime(a[3])) ^               a[3] ^ 
                           xtime(xtime(xtime(a[0]))) ^                                    a[0])  
        
        new_state[2][j] = (xtime(xtime(xtime(a[2]))) ^ xtime(xtime(a[2])) ^ xtime(a[2]) ^ 
                           xtime(xtime(xtime(a[3]))) ^                      xtime(a[3]) ^ a[3] ^ 
                           xtime(xtime(xtime(a[0]))) ^ xtime(xtime(a[0])) ^               a[0] ^ 
                           xtime(xtime(xtime(a[1]))) ^                                    a[1])  
        
        new_state[3][j] = (xtime(xtime(xtime(a[3]))) ^ xtime(xtime(a[3])) ^ xtime(a[3]) ^ 
                           xtime(xtime(xtime(a[0]))) ^                      xtime(a[0]) ^ a[0] ^ 
                           xtime(xtime(xtime(a[1]))) ^ xtime(xtime(a[1])) ^               a[1] ^ 
                           xtime(xtime(xtime(a[2]))) ^                                    a[2])   
    
    return new_state  

def state_add(state, round_key):  
    return [[s ^ k for s, k in zip(row, key_row)] for row, key_row in zip(state, round_key)]  

# AES round function  不包括加轮密钥
def aes_round(state):  
    new_state = [[0] * 4 for _ in range(4)] 
    new_state = sub_bytes(state)  
    new_state = shift_rows(new_state)  
    new_state = mix_columns(new_state)  
    return new_state  

import random  

def generate_random_state_matrix():  
    """随机生成一个4x4状态矩阵"""  
    state = [[random.randint(0, 255) for _ in range(4)] for _ in range(4)]  
    return state  

sigma = [0,7,14,11,4,13,10,1,8,15,6,3,12,5,2,9]

def sigma_function(state):
    new_state = [[0] * 4 for _ in range(4)]
    index = 0
    for i in range(4):
        for j in range(4): 
            new_index = sigma[index]  
            new_row, new_col = divmod(new_index, 4)   
            new_state[new_row][new_col] = state[i][j]  
            index += 1  
            #new_state[sigma[4*i+j]//4][sigma[4*i+j]%4] = state[i][j]
    return new_state

def invers_sigma_function(state):
    new_state = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = state[sigma[4*i+j]//4][sigma[4*i+j]%4]
    return new_state


def Pi_function(A1, A2, A3, M):
    new_A1 = sigma_function(state_add(A2, state_add(A3, M)))
    new_A2 = state_add(aes_round(A1), M)
    new_A3 = state_add(aes_round(A2), M)
    return new_A1, new_A2, new_A3
    
    
if __name__ == '__main__':  

    for t in range(2**11):

        k0 = generate_random_state_matrix()
        k1 = generate_random_state_matrix()
        IV = generate_random_state_matrix()
        k_0 = generate_random_state_matrix()
        k_1 = generate_random_state_matrix()
        IV1 = generate_random_state_matrix()
        
        c = [[0 for _ in range(4)] for _ in range(4)]
        c[0][0] = 1
        
        A1_0 = k1
        A2_0 = k0
        A3_0 = IV
        A_1_0 = k_1
        A_2_0 = k_0
        A_3_0 = IV1
        
        for i in range(9):  #initialisation
            A1_0, A2_0, A3_0 = Pi_function(A1_0, A2_0, A3_0, c)
            A_1_0, A_2_0, A_3_0 = Pi_function(A_1_0, A_2_0, A_3_0, c)
        A1_0, A2_0, A3_0 = state_add(A1_0, k1), state_add(A2_0, k0), state_add(A3_0, IV)
        A_1_0, A_2_0, A_3_0 = state_add(A_1_0, k_1), state_add(A_2_0, k_0), state_add(A_3_0, IV1)    
            
        D1 = aes_round(A1_0)
        D1 = state_add(D1, aes_round(A_1_0))
        D1 = state_add(D1, aes_round(A2_0))
        D1 = state_add(D1, aes_round(A_2_0))
         
        D1 = inverse_shift_rows(inverse_mix_columns(D1))
        
        A1_temp = aes_round(A1_0)
        A_1_temp= aes_round(A_1_0)
        
        state = [[0 for _ in range(4)] for _ in range(4)]  
        success= [[1 for _ in range(4)] for _ in range(4)]
        
        M0 = generate_random_state_matrix()
        M_0= generate_random_state_matrix()
    
        for i in range(4):
            false = 0
            for j in range(4):
                for m0 in range(2**8):   
                    M0[i][j] = (M0[i][j] + 1) & 0xff
                    temp1 = sbox[(A1_temp[i][j] ^ M0[i][j]) >> 4][(A1_temp[i][j] ^ M0[i][j]) & 0x0F] ^ D1[i][j]
                    M_0[i][j] = inverse_sbox[temp1>>4][temp1 & 0x0F] ^ A_1_temp[i][j]

                    if sbox[(A2_0[i][j] ^ A3_0[i][j] ^ M0[i][j]) >> 4][(A2_0[i][j] ^ A3_0[i][j] ^ M0[i][j]) & 0x0F] ^ sbox[(A_2_0[i][j] ^ A_3_0[i][j] ^ M_0[i][j]) >> 4][(A_2_0[i][j] ^ A_3_0[i][j] ^ M_0[i][j]) & 0x0F] == D1[sigma[4*i+j]//4][sigma[4*i+j]%4]:
                        #print(i, j, 'get')
                        state[i][j]=1
                        break
                if state[i][j] == 0:
                    false = 1
                    break
            if false == 1:
                break
                    
        if state == success:
            D1 = mix_columns(shift_rows(D1))
            M1 = [[0 for _ in range(4)] for _ in range(4)]
            M_1= state_add(M1, D1)
            
            A1_1, A2_1, A3_1 = Pi_function(A1_0, A2_0, A3_0, M0)
            A_1_1, A_2_1, A_3_1 = Pi_function(A_1_0, A_2_0, A_3_0, M_0)
            A1_2, A2_2, A3_2 = Pi_function(A1_1, A2_1, A3_1, M1)
            A_1_2, A_2_2, A_3_2 = Pi_function(A_1_1, A_2_1, A_3_1, M_1)
            
            print("!!!success!!!")
            with open('SMAC committing attack.txt', 'w') as f:
                """K and IV"""
                print("K 0", file=f)
                for row in k0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("K 1", file=f)
                for row in k1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("IV", file=f)
                for row in IV:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("K' 0", file=f)
                for row in k_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("K' 1", file=f)
                for row in k_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("IV'", file=f)
                for row in IV1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                
                """massage"""
                print("M 0", file=f)
                for row in M0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("M' 0", file=f)
                for row in M_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("M 1", file=f)
                for row in M1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("M' 1", file=f)
                for row in M_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                
                """state time 0"""
                print("A 1 0", file=f)
                for row in A1_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 2 0", file=f)
                for row in A2_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 3 0", file=f)
                for row in A3_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 1 0", file=f)
                for row in A_1_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 2 0", file=f)
                for row in A_2_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 3 0", file=f)
                for row in A_3_0:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                
                """state time 1"""
                print("A 1 1", file=f)
                for row in A1_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 2 1", file=f)
                for row in A2_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 3 1", file=f)
                for row in A3_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 1 1", file=f)
                for row in A_1_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 2 1", file=f)
                for row in A_2_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 3 1", file=f)
                for row in A_3_1:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
    
                """state time 2"""
                print("A 1 2", file=f)
                for row in A1_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 2 2", file=f)
                for row in A2_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A 3 2", file=f)
                for row in A3_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 1 2", file=f)
                for row in A_1_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 2 2", file=f)
                for row in A_2_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)
                print("A' 3 2", file=f)
                for row in A_3_2:  
                    print(['{:02x}'.format(b) for b in row], file=f) 
                print('\n', file=f)

            break











