# encryptImage


## Codigo original obtenido de https://www.thesecuritybuddy.com/cryptography-and-python/how-to-encrypt-and-decrypt-an-image-using-python/

### Ese fue la pagina que usé para obtener el ejemplo, lo que hace es cifrar una imagen utilizando el algoritmo AES en modo CBC (Cipher Block Chaining). El código original da las funciones para cifrar y descifrar imagenes, empieza generando una clave y un vector de inicialización (IV) aleatorios, luego cifra los datos binarios de la imagen y guarda el resultado en un nuevo archivo. Al final descifra el archivo cifrado usando la misma clave y IV para recuperar la imagen original. Solo que tuve que modificar y agregar ciertas cosas para que el código funcione bien.

#### Primero importamos los módulos necesarios (os y Crypto.Cipher.AES).

#### Luego, al guardar y leer datos binarios tenemos que abrir los archivos en modo binario, wb para escritura y rb para lectura.

#### Agregamos una función pad para que los datos se ajusten al tamaño de bloque requerido por AES.

#### Implementé la funcion de decrypt porque no estaba definida en el ejemplo

En el último commit lo que le agregué al codigo ya mofificado fueron mejoras en la robustez y seguridad. Añadí una verificación para asegurarse de que los archivos existen antes de intentar usarlos, evitando errores. Despues, añadí un manejo de errores durante la desencriptación para manejar casos donde los datos cifrados podrían estar corruptos o no ser válidos, lo que podría lanzar una excepción. Esos cambios sirven para que el código sea más seguro y confiable dando retroalimentación clara sobre los errores.
