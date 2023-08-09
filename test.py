import sqlite3

class DBase:
    def __init__(self):
        self._con = sqlite3.connect("database/snake.db", detect_types=sqlite3.PARSE_DECLTYPES)
        self.create_tables()

    def is_table_exist(self, tbl_name):
        db = self._con.cursor()
        cursor = db.execute("SELECT * FROM sqlite_master WHERE name = ?", (tbl_name,))

        if cursor.fetchone():
            #print("테이블이 있어요")
            self._con.commit()
            db.close()
            return True

        #print("테이블이 없어요")
        self._con.commit()
        db.close()
        return False

    def create_tables(self):
        db = self._con.cursor()
        if self.is_table_exist('material') == False:
            Log.Print("Material table create")
            sql = "CREATE TABLE material (idx INTEGER PRIMARY KEY, name TEXT, description TEXT, del INTEGER)"
            db.execute(sql)

        if self.is_table_exist('gradation') == False:
            Log.Print("Gradation table create")
            sql = "CREATE TABLE gradation (idx INTEGER PRIMARY KEY, name TEXT, desc TEXT, comb_img BLOB, tbl_img BLOB, " \
                  "ui_imgred BLOB, ui_imggreen BLOB, org_img BLOB, org_mask_up BLOB, org_mask_down BLOB, " \
                  "del INTEGER)"
            db.execute(sql)

        if self.is_table_exist('project') == False:
            Log.Print("project table create")
            sql = "CREATE TABLE project (idx INTEGER PRIMARY KEY, projectname TEXT, filename TEXT, " \
                  "date_time text DEFAULT(datetime('now', 'localtime')), outfilename TEXT," \
                  "cutting REAL, overlap REAL, gradation_idx INTEGER, material_idx INTEGER, " \
                  "curve1 ARRAY, curve2 ARRAY, del INTEGER)"
            db.execute(sql)

        if self.is_table_exist('profile') == False:
            Log.Print("profile table create")
            sql = "CREATE TABLE profile (idx INTEGER PRIMARY KEY, hist_idx INTEGER, name TEXT, " \
                  "cutting REAL, overlap REAL, gradation_idx INTEGER, material_idx INTEGER, " \
                  "curve1 ARRAY, curve2 ARRAY, del INTEGER)"
            db.execute(sql)

        if self.is_table_exist('file_path') == False:
            Log.Print("file path create")
            sql = "CREATE TABLE file_path (idx INTEGER PRIMARY KEY, name TEXT, path TEXT)"
            db.execute(sql)

        self._con.commit()
        db.close()

