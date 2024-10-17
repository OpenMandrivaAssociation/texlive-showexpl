Name:		texlive-showexpl
Version:	57414
Release:	2
Summary:	Typesetting LaTeX source code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showexpl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showexpl.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/showexpl
%doc %{_texmfdistdir}/doc/latex/showexpl
#- source
%doc %{_texmfdistdir}/source/latex/showexpl

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
