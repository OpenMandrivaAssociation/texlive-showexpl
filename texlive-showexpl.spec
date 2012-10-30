# revision 27790
# category Package
# catalog-ctan /macros/latex/contrib/showexpl
# catalog-date 2012-09-23 11:23:18 +0200
# catalog-license lppl
# catalog-version v0.3j
Name:		texlive-showexpl
Version:	v0.3j
Release:	1
Summary:	Typesetting LaTeX source code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showexpl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a way to typeset LaTeX source code and
the related result in the same document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showexpl/showexpl.sty
%doc %{_texmfdistdir}/doc/latex/showexpl/README
%doc %{_texmfdistdir}/doc/latex/showexpl/result-picture.pdf
%doc %{_texmfdistdir}/doc/latex/showexpl/showexpl-test.pdf
%doc %{_texmfdistdir}/doc/latex/showexpl/showexpl-test.tex
%doc %{_texmfdistdir}/doc/latex/showexpl/showexpl.cfg
%doc %{_texmfdistdir}/doc/latex/showexpl/showexpl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/showexpl/showexpl.dtx
%doc %{_texmfdistdir}/source/latex/showexpl/showexpl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
