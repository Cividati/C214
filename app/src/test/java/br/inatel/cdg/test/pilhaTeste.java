package br.inatel.cdg.test;

import br.inatel.cdg.Pilha;
import org.junit.Test;

import static org.junit.Assert.*;


public class pilhaTeste {

    @Test
    public void testePilhaVazia(){
        Pilha<Integer> pilhaInteiros = new Pilha<Integer>();
        boolean vazia = pilhaInteiros.pilhaVazia();
        assertTrue(vazia);

    }

    @Test
    public void testePilhaNaoVazia(){
        Pilha<Integer> pilhaInteiros = new Pilha<Integer>();
        pilhaInteiros.push(1);
        boolean vazia = pilhaInteiros.pilhaVazia();
        assertFalse(vazia);

    }

    @Test
    public void testePilhaPush(){
        Pilha<Integer> pilhaInteiros = new Pilha<Integer>();
        boolean vazia = pilhaInteiros.pilhaVazia();
        pilhaInteiros.push(10);
        int tamanho = pilhaInteiros.size();
        assertEquals(1, tamanho);

    }

}
