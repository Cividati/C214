package br.inatel.cdg.test.mockito;

import br.inatel.cdg.test.BuscaInimigo;
import br.inatel.cdg.test.Inimigo;
import br.inatel.cdg.test.InimigoConst;
import br.inatel.cdg.test.InimigoService;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.MockitoJUnitRunner;

import static org.junit.Assert.assertEquals;

@RunWith(MockitoJUnitRunner.class)
public class TesteBuscaInimigo {

    @Mock
    private InimigoService service;
    private BuscaInimigo buscaInimigo;

    @Before
    public void setup() {
        buscaInimigo = new BuscaInimigo(service);
    }

    @Test
    public void testeBuscaInimigoSkeleton() {
        Mockito.when(service.busca(10)).thenReturn(InimigoConst.SKELETON);
        //Fiz a busca
        Inimigo skeleton = buscaInimigo.buscaInimigo(10);

        //Faz assertion
        assertEquals("Skeleton", skeleton.getNome());
        assertEquals(200.0, skeleton.getQtdVida(), 0.1);
        assertEquals("Espada do Skeleton", skeleton.getArma());

    }
}
