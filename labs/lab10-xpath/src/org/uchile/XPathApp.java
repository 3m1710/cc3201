package org.uchile;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringWriter;
import java.sql.SQLException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class XPathApp {
	private static final String KILL = "-k";


	public static void main(String[] args) throws SQLException, IOException, ParserConfigurationException, SAXException{
		if(args.length!=1){
			System.err.println("Hay que dar el nombre del archivo XML como un argumento");
			return;
		}
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		DocumentBuilder builder = factory.newDocumentBuilder();
		Document doc = builder.parse(new File(args[0]));

		BufferedReader br_std_in = new BufferedReader(new InputStreamReader(System.in,"utf-8"));

		XPathFactory xPathfactory = XPathFactory.newInstance();
		XPath xpath = xPathfactory.newXPath();

		while(true){
			System.out.println("Ingrese una expresion en XPath:");
			String input = br_std_in.readLine().trim();
			if(input.equals(KILL)) break;

			try{
				XPathExpression expr = xpath.compile(input);
				try{
					NodeList nl = (NodeList)expr.evaluate(doc, XPathConstants.NODESET);
					if(nl.getLength()==0){
						System.out.println("No hay resultados");
					} else {
						for(int i=0; i<nl.getLength(); i++){
							System.out.println(nodeToString(nl.item(i)));
						}
					}
				} catch(Exception e){
					// an aggregation query perhaps
					// cannot return NodeSet
					System.out.println(expr.evaluate(doc));
				}
			} catch(Exception e){
				e.printStackTrace();
			} 

			System.out.println("");
		}
		br_std_in.close();
	}

	private static String nodeToString(Node node) {
		if(node.getNodeType()==Node.ELEMENT_NODE){
			StringWriter sw = new StringWriter();
			try {
				Transformer t = TransformerFactory.newInstance().newTransformer();
				t.setOutputProperty(OutputKeys.OMIT_XML_DECLARATION, "yes");
				t.transform(new DOMSource(node), new StreamResult(sw));
			} catch (TransformerException te) {
				System.out.println("nodeToString Transformer Exception");
			}
			return sw.toString();
		} else{
			return node.toString();
		}
	}
}