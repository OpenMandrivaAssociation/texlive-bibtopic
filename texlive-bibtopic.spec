# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bibtopic
# catalog-date 2006-10-17 00:49:54 +0200
# catalog-license gpl
# catalog-version 1.1a
Name:		texlive-bibtopic
Version:	1.1a
Release:	6
Summary:	Include multiple bibliographies in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibtopic
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to include several bibliographies
covering different 'topics' or bibliographic material into a
document (e.g., one bibliography for primary literature and one
for secondary literature). The package provides commands to
include either all references from a .bib file, only the
references actually cited or those not cited in your document.
The user has to construct a separate .bib file for each
bibliographic 'topic', each of which will be processed
separately by BibTeX. If you want to have bibliographies
specific to one part of a document, see the packages bibunits
or chapterbib.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibtopic/bibtopic.sty
%doc %{_texmfdistdir}/doc/latex/bibtopic/README
%doc %{_texmfdistdir}/doc/latex/bibtopic/articles.bib
%doc %{_texmfdistdir}/doc/latex/bibtopic/bibtopic.pdf
%doc %{_texmfdistdir}/doc/latex/bibtopic/books.bib
%doc %{_texmfdistdir}/doc/latex/bibtopic/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/bibtopic/bibtopic.dtx
%doc %{_texmfdistdir}/source/latex/bibtopic/bibtopic.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 749696
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 717942
- texlive-bibtopic
- texlive-bibtopic
- texlive-bibtopic
- texlive-bibtopic
- texlive-bibtopic

