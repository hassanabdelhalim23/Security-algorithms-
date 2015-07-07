def mul_inverse(divisor, dividend):
        al_temp = dividend
        A = [divisor, dividend]
        Q = [0]
        X = []
        i = 1
        while al_temp != 0:
            Q.insert(i, A[i - 1] / A[i])
            A.insert(i + 1, A[i - 1] % A[i])
            al_temp = A[i + 1]
            i += 1

        x_length = len(Q)
        i = 0
        while i < x_length:
            if i != x_length - 2:
                X.insert(i, 0)
            else:
                X.insert(i, 1)
            i += 1

        x_length -= 3
        while x_length >= 0:
            new_x = Q[x_length + 1] * X[x_length + 1] + X[x_length + 2]
            X[x_length] = new_x
            x_length -= 1

        checker = A[0] * X[1] - A[1] * X[0]
        if checker == -1:
            return X[0]
        else:
            return -1 * X[0] % divisor


def transpose(matrix):  # supposing the matrix is squared
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[j for j in range(0, cols)] for i in range(0, rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            transposed_matrix[i][j] = matrix[j][i]

    return transposed_matrix


def change_sign(number):
    if number % 2 == 0:
        return 1
    else:
        return -1


def subMatrix(matrix, excluding_row, excluding_col):
    sub = [[j for j in range(0, len(matrix[0]) - 1)] for i in range(0, len(matrix) - 1)]
    r = -1
    for i in range(0, len(matrix)):
        if i == excluding_row:
            continue
        r += 1
        c = -1

        for j in range(0, len(matrix[0])):
            if j == excluding_col:
                continue
            c += 1
            sub[r][c] = matrix[i][j]
    return sub


def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    _sum = 0
    for i in range(0, len(matrix)):
        _sum += change_sign(i) * matrix[0][i] * det(subMatrix(matrix, 0, i))

    return _sum


def cofactor(matrix):
    _cofactor = [[j for j in range(0, len(matrix[0]))] for i in range(0, len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            _cofactor[i][j] = change_sign(i) * change_sign(j) * det(subMatrix(matrix, i, j))
    return _cofactor


def matrix_inverse(matrix):
    adjugate_matrix = [[j % 26 for j in i] for i in transpose(cofactor(matrix))]
    matrix_det = det(matrix) % 26
    _mul_inverse = mul_inverse(26, matrix_det)
    return [[_mul_inverse * j % 26 for j in i] for i in adjugate_matrix]


def matrix_multiplication(matrix1, matrix2, m1_rows, m2_rows, m2_cols):

    result = [[j for j in range(0, m2_cols)] for i in range(0, m1_rows)]

    for i in range(0, m1_rows):
        for j in range(0, m2_cols):
            for k in range(0, m2_rows):
                # print "[i][k] = [", i, "][", k, "], [k][j] = [", k, "][", j, "]"
                # print matrix1[i][k], matrix2[k]
                result[i][j] += matrix1[i][k] * matrix2[k]
    return result

def text_to_numeric(text, dividend):
    counter = 0
    result = []
    for i in range(0, int(round(len(text) / float(dividend)))):
        z = []
        for j in range(0, dividend):
            try:
               z.insert(j, ord(text[counter]) - 97)
            except IndexError:
                z.insert(j, 0)
            counter += 1
        result.insert(i, z)
    return result


def enc(message, key, key_dimension):
    message = message.lower().replace(" ", "")
    key = key.lower().replace(" ", "")
    final_message = ""
    if key_dimension == 2:
        key_numerical = text_to_numeric(key, 2)
        msg_numerical = text_to_numeric(message, 2)
        for i, msg in enumerate(msg_numerical):
            result = matrix_multiplication(key_numerical, msg, 2, 2, 1)
            final_message += str(chr(result[0][0] + 97))
            final_message += str(chr(result[1][0] + 97))
    else:
        key_numerical = text_to_numeric(key, 3)
        msg_numerical = text_to_numeric(message, 3)
        for i, msg in enumerate(msg_numerical):
            result = matrix_multiplication(key_numerical, msg, 3, 3, 1)
            result = [[row[j] % 26 for j, value in enumerate(row)] for i, row in enumerate(result)]
            final_message += str(chr(result[0][0] + 97))
            final_message += str(chr(result[1][0] + 97))
            final_message += str(chr(result[2][0] + 97))
    return final_message


def dec(message, key, key_dimension):
    message = message.lower().replace(" ", "")
    key = key.lower().replace(" ", "")
    final_message = ""
    if key_dimension == 2:
        key_numerical = text_to_numeric(key, 2)
        msg_numerical = text_to_numeric(message, 2)
        key_inverse = matrix_inverse(key_numerical)
        for i, msg in enumerate(msg_numerical):
            result = matrix_multiplication(key_inverse, msg, 2, 2, 1)
            final_message += str(chr(result[0][0] + 97))
            final_message += str(chr(result[1][0] + 97))
    else:
        key_numerical = text_to_numeric(key, 3)
        msg_numerical = text_to_numeric(message, 3)
        key_inverse = matrix_inverse(key_numerical)
        for i, msg in enumerate(msg_numerical):
            result = matrix_multiplication(key_inverse, msg, 3, 3, 1)
            result = [[row[j] % 26 for j, value in enumerate(row)] for i, row in enumerate(result)]
            final_message += str(chr(result[0][0] + 97))
            final_message += str(chr(result[1][0] + 97))
            final_message += str(chr(result[2][0] + 97))
    return final_message

#print dec("afxzdxnjlbbp", "bdbbbccde", 3)
#print dec("eifdgfrmtfex", "bdbbbccde", 3)
