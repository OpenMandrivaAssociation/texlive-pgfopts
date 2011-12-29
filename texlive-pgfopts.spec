# revision 23320
# category Package
# catalog-ctan /macros/latex/contrib/pgfopts
# catalog-date 2011-06-03 00:21:14 +0200
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-pgfopts
Version:	2.1
Release:	1
Summary:	LaTeX package options with pgfkeys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfopts
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfopts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pgfkeys package (part of the pgf distribution) is a well-
designed way of defining and using large numbers of keys for
key-value syntaxes. However, pgfkeys itself does not offer
means of handling LaTeX class and package options. This package
adds such option handling to pgfkeys, in the same way that
kvoptions adds the same facility to the LaTeX standard keyval
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgfopts/pgfopts.sty
%doc %{_texmfdistdir}/doc/latex/pgfopts/README
%doc %{_texmfdistdir}/doc/latex/pgfopts/pgfopts.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pgfopts/pgfopts.dtx
%doc %{_texmfdistdir}/source/latex/pgfopts/pgfopts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
