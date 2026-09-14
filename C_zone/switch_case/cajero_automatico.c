#include <stdio.h>
int main(){
    
    float dep, ret;
    float saldo = 2000;
    int opc;
    
    do{
        printf("Bienvenido a tu cajero. ¿Qué operación deseas hacer?\n\n");
        printf("1. Consultar Saldo\n");
        printf("2. Depositar\n");
        printf("3. Retirar\n");
        printf("4. Salir\n\n:");
        scanf("%d", &opc);
        
        switch(opc){
            case 1:
                    printf("\n== CONSULTAR SALDO ==\n\n");
                    printf("Saldo disponible en la cuenta: %.2f MXN\n\n", saldo);
                    break;
            case 2:
                    printf("\n== DEPOSITAR ==\n\n");
                    printf("Ingrese la cantidad que desea depositar:\n");
                    scanf("%f", &dep);
                    if(dep>0){
                        saldo = saldo + dep;
                        printf("\nDeposito exitoso.\n\n");
                    }else{
                        printf("Error. Cantidad Invalida. Volviendo al menu...\n\n");
                    }
                    break;
            case 3:
                    printf("\n== RETIRAR ==\n\n");
                    printf("Ingrese la cantidad que desea retirar:\n");
                    scanf("%f", &ret);
                    if(ret>0 && ret <= saldo){
                        saldo = saldo - ret;
                        printf("\nRetiro exitoso.\n\n");
                    }else{
                        printf("Error. Cantidad Invalida. Volviendo al menu...\n\n");
                    }
                    break;
            case 4:
                    printf("\nGracias por usar el cajero, buen día.\n");
                    break;
            default:
                    printf("Error, opción no valida.\n\n");
                    break;
        }
    }while(opc!=4);
    
    return 0;
}