Name:		texlive-bibtopic
Version:	15878
Release:	1
Summary:	Include multiple bibliographies in a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibtopic
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibtopic.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
