package br.inatel.cdg;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class Pilha<T> {
    private List<T> elementos = new ArrayList<T>();
    private int tamanho;

    public int size(){
        return tamanho;
    }

    public boolean pilhaVazia(){ return (tamanho == 0); }

    public void push(T elem){
        elementos.add(elem);
        this.tamanho++;
    }

    public void  pop(){

        if (pilhaVazia()){
            throw new EmptyStackException();
        }

        this.elementos.remove(tamanho-1);
        this.tamanho--;
    }
}
