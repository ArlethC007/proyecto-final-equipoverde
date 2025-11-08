from database.db_connection import get_db_connection
class VentaModel:
    @staticmethod
<<<<<<< HEAD:models/venta_moodel.py
    def agregar_venta(cliente_id, usuario_id, productos):
        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute('''INSERT INTO ventas (cliente_id, usuario_id, productos) VALUES (?,?,?)''', (cliente_id, usuario_id, productos))
        venta_id=cursor.lastrowid
        conn.commit()
        conn.close()
        return venta_id
    @staticmethod
    def obtener_ventas(fecha_inicio=None, fecha_fin=None):
        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute('''''')
    @staticmethod
    def obtener_detalle_venta(venta_id):pass
    @staticmethod
    def eliminar_venta(venta_id):pass
=======
    def agregar_venta(cliente_id, usuario_id, productos):pass
        
    @staticmethod
    def obtener_ventas(fecha_inicio=None, fecha_fin=None):pass
        
    @staticmethod
    def obtener_detalle_venta(venta_id):pass
        
    @staticmethod
    def eliminar_venta(venta_id):pass
>>>>>>> 535daeb10abee1d139799a9112c1769e587bf3fa:nailstock/models/venta_moodel.py
