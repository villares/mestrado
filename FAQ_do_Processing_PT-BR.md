##FAQ do Processing

#### O que é o *sketchbook*? o que vocês querem dizer com *sketches*?

Nós pensamos que a maioria dos "ambientes integrados de desenvolvimento" (Microsoft Visual Studio, Xcode, Eclipse, etc.) tendem a ser exagerados para o tipo de audiência em que miramos com Processing. por essa razão, nós introduzimos o 'sketchbook' (um caderno de croquis) que é uma maneira mais leve de organizar projetos. Com a formação de designers, gostaríamos que o processo de programação fosse muito como desenhar um croquis. A configuração do sketchbook, e a ideia de só sentar e escrever código (sem ter que escrever duas páginas para configurar um cotexto gráfico, estabelecer uma linha de execução e etc.) é um passo na direção deste objetivo.

A ideia de apenas escrever um pequeno trecho de código que executa muito facilmente (pro meio de um pequeno botão de executar) é uma descendente direta do trabalho de John Maeda em Design by Numbers, e nossas experiências o mantendo. (Sim, outras linguagens e ambientes fizeram isso primeiro, mas no nosso caso o conceito é tirado do DBN.)

#### Porque Java? Ou porque uma linguagem de progamação tão Java-esca?

We didn't set out to make the ultimate language for visual programming, we set out to make something that was:

1. A sketchbook for our own work, simplifying the majority of tasks that we undertake,
2. A teaching environment for that kind of process, and
3. A point of transition to more complicated or difficult languages like full-blown Java or C++ (a gateway drug to more geekier and more difficult things)

At the intersection of these points is a tradeoff between speed and simplicity of use. i.e. if we didn't care about speed, Python, Ruby or many other scripting languages would make far more sense (especially for the simplicity and education aspect of it). If we didn't care about transition to more advanced languages, we'd get rid of the C-style (well,[ Algol](http://en.wikipedia.org/wiki/Algol_60), really) syntax. etc etc.

Java makes a nice starting point for a sketching language because it's far more forgiving than C++ and also allows users to export sketches for distribution across many different platforms. When we got started in 2001, most people were using it to build[ applets that ran on the web](http://processing.org/exhibition/curated_page_1.html), which was important to the early growth of the project.

Processing is not intended as the ultimate environment or language (in fact, the language is just Java, but with a new graphics and utility API along with some simplifications). Fundamentally, Processing just assembles our experience in building things, and trying to simplifies the parts that we felt should be easier.

#### Eu conhecó Java, isso aqui é Java? Como eu uso desta maneira?

O código em Processing  é convertido diretamente em código Java (usando o "pré-processador") quando você aciona o botão Executar. This also makes it possible to embed other Java code in your sketches, or use the core.jar file from the Processing distribution to develop your own sketches with other environments. For instance, if you want to use[ Eclipse](http://eclipse.org/), there's a[ tutorial](http://processing.org/learning/eclipse/) on the Processing site.

The main rule when using Java code: You cannot use most of the AWT or Swing (which is built on the AWT), because it will interfere with the graphics model. If you want to add scroll bars and buttons to your projects, you should make them using Processing code, or embed your Processing applet inside another Swing or AWT application (see below). Even if they appear to work, such sketches will usually break when you try to run on other operating systems or other versions of Java.

Since we can't really support anything and everything that you might want to do when interfacing with Java or using core.jar inside a Java environment, we have a separate[ discussion area](http://forum.processing.org/two/categories/hardware-other-languages) on the discourse forum for asking questions related to using Processing to interface with regular Java code.

If you want to embed Processing into another Java application, visit the developer's reference for[ PApplet](http://dev.processing.org/reference/core/javadoc/processing/core/PApplet.html). A discussion of how to use Processing with Eclipse is found[ here](http://processing.org/discourse/yabb2/YaBB.pl?board=Integrate;action=display;num=1117133941).

Also note that when using the Processing API or libraries outside the PDE, the headaches of the Java CLASSPATH and PATH return, and using libraries gets much nastier. These are some of the headaches that we try to hide in the Processing environment, things that separate Processing from straight Java coding. We feel that it is important to put the good stuff at the surface, and that those details don't teach students much anyway (and they annoy advanced users too).

#### De onde vem este projeto? Isto é  DBN?

Processing  é descendente do projeto  [ Design By Numbers](https://web.archive.org/web/20030923172031/http://dbn.media.mit.edu/) (DBN)  de outras iniciativas no grupo Aesthetics + Computation Group (ACG, Grupo Estética + Computação no MIT). DBN is a simplified programming language that was developed to teach the structure and interpretation of software in a visual manner. Design By Numbers was created by John Maeda and accompanied a book of the same name. While at the ACG, Ben and Casey were involved in the development and maintenance of the DBN software and courseware, and that experience provided the basis for the Processing project.

While working on DBN, Ben developed several experimental versions that included other programming languages (Python and Scheme) and drawing features (color, changing the window size, magnification, movie recording, and even OpenGL support), but it was clear that these did not make sense for the DBN project because they interfered with Maeda's intention of a simplified programming language and environment.

Na época (entre 1998-2000), o trabalho no ACG era normalmente desenvolvido via sketches escritos em Java e posteriormente movidos para aplicativos escritos em  C++ usando OpenGL.Nós estávamos interessados em fundir a ideia de "sketching" em código com o aspecto pefagógico do DBN. O desenvolvimento do Processing começou formalmente na primavera de 2001 com discusÕes entre Casey and Ben sobre API e conjunto de  recursos, e as primeiras versões do Processing (versões 0001, 0003, e 0005) foram usadas em  agosto de 2001 no workshop na Universidade Musashino de Arte no Japão.