package org.uchile;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.Properties;

public class NotaAppSegura {
    private static final String HOST = "cc3201.dcc.uchile.cl";
    private static final String PORT = "5432"; // o 5440
    private static final String DATABASE = "cc3201";
    private static final String CONNECTION_URL = "jdbc:postgresql://"+HOST+":"+PORT+"/"+DATABASE;
    private static final String USERNAME = "cc3201";
    private static final String PASSWORD = "je_<3_cc3201";
    private static final String SSL = "true";

    private static final String KILL = "-k";


    public static void main(String[] args) throws SQLException, IOException{
        String url = CONNECTION_URL;

        Properties props = new Properties();
        props.setProperty("user",USERNAME);
        props.setProperty("password",PASSWORD);
        props.setProperty("ssl",SSL);

        // la siguiente propiedad es para deshabilitar la validaci�n de
        // certificados en SSL (normalmente, no se recomienda, pero en el lab,
        // ser� complejo instalar un certificado en cada truststore)
        props.setProperty("sslfactory","org.postgresql.ssl.NonValidatingFactory");
        Connection conn = DriverManager.getConnection(url, props);

        // esta vez vamos a preparar el "statement" antes
        // luego reemplezaremos los '?' con los valores de entrada
        PreparedStatement pSt = conn.prepareStatement("SELECT nota, nombre, comentario FROM nota.bdd2018 WHERE id=?");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in,"utf-8"));

        try{
            while(true){
                System.out.println("Ingrese un apellido paterno y pulse [Intro] (o '"+KILL+"' para matar):");

                String input = br.readLine().trim();
                if(input.equals(KILL)) break;
                int in = Integer.parseInt(input);
                pSt.setInt(1, in);

                // executar una consulta
                System.out.println("=== Ejeuctando la consulta: "+pSt+" ===");
                ResultSet rs = pSt.executeQuery();

                System.out.println("=== Resultados ===");

                System.out.println("\n-- Esquema --");
                ResultSetMetaData rsm = rs.getMetaData();
                for(int i=1; i<=rsm.getColumnCount(); i++){ // las columnas empiezan con 1
                    if(i!=1)
                        System.out.print("\t");
                    System.out.print(rsm.getColumnLabel(i)+":"+rsm.getColumnTypeName(i));
                }

                System.out.println("\n\n-- Datos --");
                while (rs.next()){ // mover el cursor a la proxima posici�n (y devolver true si hay una tupla m�s)
                    System.out.println();
                    System.out.print(Math.round((rs.getFloat(1)-1)*100/6.0));
                    System.out.print("\t");
                    for(int i=2; i<=rsm.getColumnCount(); i++){ // las columnas empiezan con 1
                        if(i!=2)
                            System.out.print("\t");
                        System.out.print(rs.getString(i));
                    }
                }

                System.out.println("\n==============================\n\n\n");
                rs.close();
            }
        } catch(Exception e){
            e.printStackTrace();
        } finally {
            try{
                pSt.close();
                br.close();
            } finally {
                conn.close();
                System.out.println("///////////////////////// Terminado.");
            }
        }
    }
}
