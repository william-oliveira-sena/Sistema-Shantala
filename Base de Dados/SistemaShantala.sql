PGDMP  $                    |            Shantala    16.4    16.4     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    Shantala    DATABASE     �   CREATE DATABASE "Shantala" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Shantala";
                postgres    false            �            1259    16398    alunos    TABLE     W  CREATE TABLE public.alunos (
    idaluno integer NOT NULL,
    nome character varying(90) NOT NULL,
    endereco character varying(120) NOT NULL,
    numero integer NOT NULL,
    telefone character varying(90) NOT NULL,
    nascimento date,
    cpf character varying(15) NOT NULL,
    rg character varying(15),
    cu character varying(15)
);
    DROP TABLE public.alunos;
       public         heap    postgres    false            �            1259    16453    alunosturma    TABLE     �   CREATE TABLE public.alunosturma (
    idalunoturma integer NOT NULL,
    idturma integer NOT NULL,
    idaluno integer NOT NULL
);
    DROP TABLE public.alunosturma;
       public         heap    postgres    false            �            1259    16408    cursos    TABLE     �   CREATE TABLE public.cursos (
    idcurso integer NOT NULL,
    nomecurso character varying(30) NOT NULL,
    duracao character varying(30) NOT NULL
);
    DROP TABLE public.cursos;
       public         heap    postgres    false            �            1259    16413 
   frequencia    TABLE     �   CREATE TABLE public.frequencia (
    idfrequencia integer NOT NULL,
    dias integer,
    horarioinicio time without time zone,
    horariofim time without time zone
);
    DROP TABLE public.frequencia;
       public         heap    postgres    false            �            1259    16418    professores    TABLE     o   CREATE TABLE public.professores (
    idprofessor integer NOT NULL,
    nomeprofessor character varying(90)
);
    DROP TABLE public.professores;
       public         heap    postgres    false            �            1259    16423    turmas    TABLE     �   CREATE TABLE public.turmas (
    idturma integer NOT NULL,
    idcurso integer NOT NULL,
    idprofessor integer NOT NULL,
    idfrequencia integer NOT NULL,
    data_inicio date
);
    DROP TABLE public.turmas;
       public         heap    postgres    false            �          0    16398    alunos 
   TABLE DATA           d   COPY public.alunos (idaluno, nome, endereco, numero, telefone, nascimento, cpf, rg, cu) FROM stdin;
    public          postgres    false    215   �       �          0    16453    alunosturma 
   TABLE DATA           E   COPY public.alunosturma (idalunoturma, idturma, idaluno) FROM stdin;
    public          postgres    false    220   �       �          0    16408    cursos 
   TABLE DATA           =   COPY public.cursos (idcurso, nomecurso, duracao) FROM stdin;
    public          postgres    false    216   �       �          0    16413 
   frequencia 
   TABLE DATA           S   COPY public.frequencia (idfrequencia, dias, horarioinicio, horariofim) FROM stdin;
    public          postgres    false    217           �          0    16418    professores 
   TABLE DATA           A   COPY public.professores (idprofessor, nomeprofessor) FROM stdin;
    public          postgres    false    218           �          0    16423    turmas 
   TABLE DATA           Z   COPY public.turmas (idturma, idcurso, idprofessor, idfrequencia, data_inicio) FROM stdin;
    public          postgres    false    219   ;        .           2606    16402    alunos chavepalunos 
   CONSTRAINT     V   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT chavepalunos PRIMARY KEY (idaluno);
 =   ALTER TABLE ONLY public.alunos DROP CONSTRAINT chavepalunos;
       public            postgres    false    215            8           2606    16457    alunosturma chavepalunosturma 
   CONSTRAINT     e   ALTER TABLE ONLY public.alunosturma
    ADD CONSTRAINT chavepalunosturma PRIMARY KEY (idalunoturma);
 G   ALTER TABLE ONLY public.alunosturma DROP CONSTRAINT chavepalunosturma;
       public            postgres    false    220            0           2606    16412    cursos chavepcursos 
   CONSTRAINT     V   ALTER TABLE ONLY public.cursos
    ADD CONSTRAINT chavepcursos PRIMARY KEY (idcurso);
 =   ALTER TABLE ONLY public.cursos DROP CONSTRAINT chavepcursos;
       public            postgres    false    216            2           2606    16417    frequencia chavepfrequencia 
   CONSTRAINT     c   ALTER TABLE ONLY public.frequencia
    ADD CONSTRAINT chavepfrequencia PRIMARY KEY (idfrequencia);
 E   ALTER TABLE ONLY public.frequencia DROP CONSTRAINT chavepfrequencia;
       public            postgres    false    217            4           2606    16422    professores chavepprofessores 
   CONSTRAINT     d   ALTER TABLE ONLY public.professores
    ADD CONSTRAINT chavepprofessores PRIMARY KEY (idprofessor);
 G   ALTER TABLE ONLY public.professores DROP CONSTRAINT chavepprofessores;
       public            postgres    false    218            6           2606    16427    turmas chavepturmas 
   CONSTRAINT     V   ALTER TABLE ONLY public.turmas
    ADD CONSTRAINT chavepturmas PRIMARY KEY (idturma);
 =   ALTER TABLE ONLY public.turmas DROP CONSTRAINT chavepturmas;
       public            postgres    false    219            <           2606    16463 $   alunosturma alunosturma_idaluno_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.alunosturma
    ADD CONSTRAINT alunosturma_idaluno_fkey FOREIGN KEY (idaluno) REFERENCES public.alunos(idaluno);
 N   ALTER TABLE ONLY public.alunosturma DROP CONSTRAINT alunosturma_idaluno_fkey;
       public          postgres    false    4654    215    220            =           2606    16458 $   alunosturma alunosturma_idturma_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.alunosturma
    ADD CONSTRAINT alunosturma_idturma_fkey FOREIGN KEY (idturma) REFERENCES public.turmas(idturma);
 N   ALTER TABLE ONLY public.alunosturma DROP CONSTRAINT alunosturma_idturma_fkey;
       public          postgres    false    4662    220    219            9           2606    16428    turmas turmas_idcurso_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.turmas
    ADD CONSTRAINT turmas_idcurso_fkey FOREIGN KEY (idcurso) REFERENCES public.cursos(idcurso);
 D   ALTER TABLE ONLY public.turmas DROP CONSTRAINT turmas_idcurso_fkey;
       public          postgres    false    4656    216    219            :           2606    16438    turmas turmas_idfrequencia_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.turmas
    ADD CONSTRAINT turmas_idfrequencia_fkey FOREIGN KEY (idfrequencia) REFERENCES public.frequencia(idfrequencia);
 I   ALTER TABLE ONLY public.turmas DROP CONSTRAINT turmas_idfrequencia_fkey;
       public          postgres    false    217    219    4658            ;           2606    16433    turmas turmas_idprofessor_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.turmas
    ADD CONSTRAINT turmas_idprofessor_fkey FOREIGN KEY (idprofessor) REFERENCES public.professores(idprofessor);
 H   ALTER TABLE ONLY public.turmas DROP CONSTRAINT turmas_idprofessor_fkey;
       public          postgres    false    4660    218    219            �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �     