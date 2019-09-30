# **Para Omeka sugerir em um campo termos de um vocabulário servido pelo TemaTres**



- Instalar o plugin **LcSuggest** (para Omeka Classic)
  Arquivos originais do plugin: https://github.com/omeka/plugin-LcSuggest

[procedimento normal de instalação de plugins]



- Identificar a **URL** em que o seu **vocabulário TemaTres é servido**Exemplo: http://www.lugaralgum.com/tematres/vocab/



- Alterar o arquivo arquivo do plugin na instalação do Omeka: **/models/Table/LcSuggest.php** 
  [pode ser necessário desinstalar e instalar novamente o plugin]

Exemplo da modificação abaixo:

```php
<?php
/**
 * Library of Congress Suggest
 * 
 * @copyright Copyright 2007-2012 Roy Rosenzweig Center for History and New Media
 * @license http://www.gnu.org/licenses/gpl-3.0.txt GNU GPLv3
 */

/**
 * The lc_suggests table.
 * 
 * @package Omeka\Plugins\LcSuggest
 */
class Table_LcSuggest extends Omeka_Db_Table
{
    /**
     * List of suggest endpoints made available by the Library of Congress 
     * Authorities and Vocabularies service.
     * 
     * The keys are URLs to the authority/vocabulary suggest endpoints. The 
     * values are arrays containing the authority/vocabulary name and the URL to 
     * the authority/vocabulary description page.
     * 
     * These authorities and vocabularies have been selected due to their large 
     * size and suitability to the autosuggest feature. Vocabularies not 
     * explicitly included here may be redundant or better suited as a full list 
     * controlled vocabulary.
     * 
     * @see http://id.loc.gov/
     */
    private $_suggestEndpoints = array(
        'http://vocabularios.saij.gob.ar/organigramas/ar26520/suggest.php' => array(
            'name' => 'Estructura Orgánica del Poder Ejecutivo Nacional', 
            'url'  => 'http://vocabularios.saij.gob.ar/organigramas/ar26520/', 
        ), 
        'http://id.loc.gov/authorities/suggest' => array(
            'name' => 'All Authorities', 
            'url'  => 'http://id.loc.gov', 
        ), 
/* aqui */
        'http://www.lugaralgum.com/tematres/vocab/suggest.php' => array(
            'name' => 'TTEPCV', 
            'url'  => 'http://www.lugaralgum.com/tematres/vocab/', 
        ), 
    /*    'http://id.loc.gov/vocabulary/suggest' => array(
            'name' => 'All Vocabularies', 
            'url'  => 'http://id.loc.gov', 
        ), 
        'http://id.loc.gov/authorities/subjects/suggest' => array(
            'name' => 'Library of Congress Subject Headings', 
            'url'  => 'http://id.loc.gov/authorities/subjects.html'
        ), 
        'http://id.loc.gov/authorities/names/suggest' => array(
            'name' => 'Library of Congress Names', 
            'url'  => 'http://id.loc.gov/authorities/names.html', 
        ), 
        'http://id.loc.gov/authorities/childrensSubjects/suggest' => array(
            'name' => 'Library of Congress Children\'s Subject Headings', 
            'url'  => 'http://id.loc.gov/authorities/childrensSubjects.html', 
        ), 
        'http://id.loc.gov/authorities/genreForms/suggest' => array(
            'name' => 'Library of Congress Genre Form Headings', 
            'url'  => 'http://id.loc.gov/authorities/genreForms.html', 
        ), 
                'http://vocabularios.saij.gob.ar/saij/suggest.php' => array(
            'name' => 'Tesauro SAIJ', 
            'url'  => 'http://vocabularios.saij.gob.ar/saij/demo/', 
        ), 
        'http://vocabularios.saij.gob.ar/inap/suggest.php' => array(
            'name' => 'Tesauro de administración pública', 
            'url'  => 'http://vocabularios.saij.gob.ar/inap/', 
        ), 
        'http://vocabularios.saij.gob.ar/jusbaires/suggest.php' => array(
            'name' => 'Vocabulario controlado de Biblioteca y Jurisprudencia del Consejo de la Magistratura de la CABA', 
            'url'  => 'http://vocabularios.saij.gob.ar/jusbaires/', 
        ), 
        'http://vocabularios.saij.gob.ar/ddhh/suggest.php' => array(
            'name' => 'Tesauro de derechos humanos', 
            'url'  => 'http://vocabularios.saij.gob.ar/ddhh/', 
        ), 
        'http://vocabularios.saij.gob.ar/anmthes/suggest.php' => array(
            'name' => 'Vocabulario del Archivo Nacional de la Memoria', 
            'url'  => 'http://vocabularios.saij.gob.ar/anmthes/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/sociables/suggest.php' => array(
            'name' => 'Vocabulario Latinoamericano de Ciencias Sociales', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/sociables/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/salud/suggest.php' => array(
            'name' => 'Vocabulario de Ciencias de la Salud para Argentina', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/salud/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/historiaargentina/suggest.php' => array(
            'name' => 'Tesauro de Historia Argentina', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/historiaargentina/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/deportes/suggest.php' => array(
            'name' => 'Vocabulario controlado sobre deportes', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/deportes/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/calish/suggest.php' => array(
            'name' => 'CaLiSH', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/calish/', 
        ), 

        'http://vocabularyserver.com/tadirah/es/suggest.php' => array(
            'name' => 'TaDiRAH - Taxonomía sobre Actividades de investigación digital en humanidades', 
            'url'  => 'http://vocabularyserver.com/tadirah/es/', 
        ), 
        'http://vocabularios.caicyt.gov.ar/tesinfo/suggest.php' => array(
            'name' => 'Tesauro sobre información y conocimiento', 
            'url'  => 'http://vocabularios.caicyt.gov.ar/tesinfo/', 
        ), */
    );
    
    /**
     * Find a suggest record by element ID.
     * 
     * @param int|string $elementId
     * @return LcSuggest|null
     */
    public function findByElementId($elementId)
    {
        $select = $this->getSelect()->where('element_id = ?', $elementId);
        return $this->fetchObject($select);
    }
    
    /**
     * Get the suggest endpoints.
     * 
     * @return array
     */
    public function getSuggestEndpoints()
    {
        return $this->_suggestEndpoints;
    }
}
```