// SOAP : Simple Object Access Protocol
// JAX-WS (Java API for XML Web Services)
// JAXB (Java Architecture for XML Binding)

// URL : Uniform Resource Locator > l'adresse de la ressource
// URN : Uniform Resource Name > la ressource elle-même
// URI : Uniform Resource Identifier > URL + URN

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService(targetNamespace = "http://polytech.fr")
public class MonServiceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt){
        return mt*0.9;
    }

    public double somme(@WebParam(name = "parametre1") double a, double b){
        return a+b;
    }

    public Etudiant getEtudiant(int identifiant) {
        return new Etudiant(1, "Mario", 19);
    }
}
