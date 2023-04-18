"""
Laboratorio - Manipulación de Datos usando Pandas
-------------------------------------------------- ---------------------------------------
Este archivo contiene las preguntas que se van a realizar en el laboratorio.
Use los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.
"""
importar  pandas  como  pd

tbl0  =  pd . read_csv ( "tbl0.tsv" , sep = " \t " )
tbl1  =  pd . read_csv ( "tbl1.tsv" , sep = " \t " )
tbl2  =  pd . read_csv ( "tbl2.tsv" , sep = " \t " )


def  pregunta_01 ():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?
    Rta/
    40
    """
    volver  len ( tbl0 )


def  pregunta_02 ():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?
    Rta/
    4
    """
    devolver  len ( tbl0 . columnas )


def  pregunta_03 ():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?
    Rta/
    un 8
    B 7
    C5
    D 6
    14
    Nombre: _c1, tipo de d: int64
    """
    devolver  tbl0 . grupo por ( '_c1' ). cuenta ()[ '_c0' ]


def  pregunta_04 ():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.
    Rta/
    4.625000
    B 5.142857
    C 5.400000
    D 3.833333
    E 4.785714
    Nombre: _c2, dtipo: float64
    """
    devolver  tbl0 . grupo por ( '_c1' )[ '_c2' ]. media ()


def  pregunta_05 ():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.
    Rta/
    _c1
    un 9
    B 9
    C 9
    D 7
    9
    Nombre: _c2, tipo de d: int64
    """
    devolver  tbl0 . grupo por ( '_c1' )[ '_c2' ]. máximo ()


def  pregunta_06 ():
    """
    Retorne una lista con los valores únicos de la columna _c4 del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.
    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    devolución  ordenada (
        tabl1 [ "_c4" ]. mapa (
            lambda  w : w . superior ()
        ). único ()
    )


def  pregunta_07 ():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.
    Rta/
    _c1
    un 37
    36
    27
    D 23
    67
    Nombre: _c2, tipo de d: int64
    """
    devolver  tbl0 . grupo por ( '_c1' ). suma ()[ '_c2' ]


def  pregunta_08 ():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.
    Rta/
        _c0 _c1 _c2 _c3 suma
    0 0 E 1 1999-02-28 1
    1 1 A 2 1999-10-28 3
    2 2 B 5 1998-05-02 7
    ...
    37 37 C 9 1997-07-22 46
    38 38 E 1 1999-09-28 39
    39 39 E 5 1998-01-26 44
    """
    suma_columna  =  pd . Marco de datos ({ 'suma' : tbl0 [ '_c0' ] +  tbl0 [ '_c2' ]})
    devolver  p.d. _ concat (
        [
            tabl0 ,
            suma_columna
        ],
        eje = 1
    )


def  pregunta_09 ():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.
    Rta/
        _c0 _c1 _c2 _c3 año
    0 0 E 1 1999-02-28 1999
    1 1 A 2 1999-10-28 1999
    2 2 B 5 1998-05-02 1998
    ...
    37 37 C 9 1997-07-22 1997
    38 38 E 1 1999-09-28 1999
    39 39 E 5 1998-01-26 1998
    """
    columna_año  =  pd . Marco de datos ({ 'año' : tbl0 [ '_c3' ]. mapa ( fecha lambda  : fecha . división ( '-' ) [ 0 ])})
    devolver  p.d. _ concat (
        [
            tabl0 ,
            columna_año
        ],
        eje = 1
    )


def  pregunta_10 ():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.
    Rta/
                                   _c1
      _c0
    0 A 1:1:2:3:6:7:8:9
    1 B 1:3:4:5:6:8:9
    2 C 0:5:6:7:9
    3D 1:2:3:5:5:7
    4 E 1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """ 
    tbl0cp  =  tbl0 . copiar ()
    tbl0cp [ '_c2' ] =  tbl0cp [ '_c2' ]. aplicar ( str )

    c1único  =  pd . Marco de datos ({ '_c1' : tbl0cp . sort_values ​​( by = '_c1' )[ '_c1' ]. único ()})
    
    resultado  =  pd . fusionar (
        c1único ,
        tbl0cp . grupo por ( '_c1' )[ '_c2' ]. aplicar ( ordenado ). aplicar ( ':' . unirse ),
        en = '_c1'
    )
    resultado  =  resultado . conjunto_índice ( '_c1' )

     resultado devuelto


def  pregunta_11 ():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.
    Rta/
        _c0 _c4
    0 0 b, f, g
    1 1 a,c,f
    2 2 a,c,e,f
    3 3 a,b
    ...
    37 37 a,c,e,f
    38 38 d,e
    39 39 a, d, f
    """
    tbl1cp  =  tbl1 . copiar ()

    c0único  =  pd . Marco de datos ({ '_c0' : tbl1cp . sort_values ​​( by = '_c0' )[ '_c0' ]. único ()})
    c4agrupados  =  pd . DataFrame ({ '_c4' : tbl1cp . groupby ( '_c0' )[ '_c4' ]. apply ( ordenado ). apply ( ',' . join )})
    
    resultado  =  pd . concat (
        [
            c0único ,
            c4agrupados ,
        ],
        eje = 1
    )
     resultado devuelto



def  pregunta_12 ():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.
    Rta/
        _c0 _c5
    0 0 bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1 1 aaa:3,ccc:2,ddd:0,hhh:9
    2 2 ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37 37 eee:0,fff:2,hhh:6
    38 38 eee:0,fff:9,iii:2
    39 39 ggg:3,hhh:8,jjj:5
    """
    tbl2cp  =  tbl2 . copiar ()
    tbl2cp [ '_c5' ] =  tbl2cp [ '_c5a' ] +  ':'  +  tbl2cp [ '_c5b' ]. aplicar ( lambda  x : str ( x ))
    c0único  =  pd . Marco de datos ({ '_c0' : tbl2cp . sort_values ​​( by = '_c0' )[ '_c0' ]. único ()})
    
    c5agrupados  =  pd . DataFrame ({ '_c5' : tbl2cp . groupby ( '_c0' )[ '_c5' ]. apply ( ordenado ). apply ( ',' . join )})
    
    resultado  =  pd . concat (
        [
            c0único ,
            c5 agrupados ,
        ],
        eje = 1
    )
     resultado devuelto


def  pregunta_13 ():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, computar la
    suma de tbl2._c5b por cada valor en tbl0._c1.
    Rta/
    _c1
    146
    134
    81
    D 112
    ES 275
    Nombre: _c5b, dtipo: int64
    """
    # Crear copia de los dataframes originales
    tbl0cp  =  tbl0 . copiar ()
    tbl2cp  =  tbl2 . copiar ()

    # Agrupar por '_c0' y crear una lista con los valores no repetidos. Luego crear un DataFrame
    # nombrando la columna como '_c0'
    c0único  =  pd . Marco de datos ({ '_c0' : tbl2cp . sort_values ​​( by = '_c0' )[ '_c0' ]. único ()})

    # Agrupar por '_c0' y sumar la columna '_c5b' por cada grupo. Luego crear un DataFrame
    # nombrando la columna como '_c5'
    c5malo  =  pd . Marco de datos ({ '_c5' : tbl2cp . groupby ( '_c0' )[ '_c5b' ]. agg ( suma )})

    # Concatenar los dos marcos de datos. Es posible porque tiene el mismo largo de filas (eje=1)
    tbl2computado  =  pd . concat (
        [
            c0único ,
            c5malo ,
        ],
        eje = 1
    )

    # Unir el Dataframe tbl0cp con el resultado computado del dataframe tbl0cp(tbl2computed)
    # por medio de la columna en común '_c0'
    tmp_result  =  pd . fusionar (
        tbl0cp ,
        tbl2computado ,
        en = '_c0'
    )

    # Agrupar por '_c5' y crear una lista con los valores no repetidos desde el dataframe 'tmp_result'.
    resultado  =  tmp_resultado . grupo por ( '_c1' )[ '_c5' ]. agg ( suma )

     resultado devuelto
