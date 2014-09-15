import matplotlib.pyplot as plt

# \definecolor{mpibg1}{HTML}{5D8B8A} % dark green
# \definecolor{mpibg2}{HTML}{BFDFDE} % light blue green
# \definecolor{mpibg3}{HTML}{A7C1C0} % gray green
# \definecolor{mpibg4}{HTML}{7DA9A8} % medium gray green
# \definecolor{mpired}{HTML}{990000}
# \definecolor{mpigreen}{HTML}{5C871D}
# \definecolor{mpiblue}{HTML}{006AA9}
# \definecolor{cscred}{rgb}{0.75,0,0}
# \definecolor{cscorange}{rgb}{1.0,.5625,0}

try:
    import seaborn as sns
    sns.set(style="whitegrid")
    mpilightgreen = '#BFDFDE'
    mpigraygreen = '#7DA9A8'
    # sns.set_palette(sns.dark_palette(mpigraygreen, 6, reverse=True))
    sns.set_palette('cool', 3)
except ImportError:
    print 'I recommend to install seaborn for nicer plots'


def conv_plot(abscissa, datalist, leglist=None, fit=None,
              markerl=None, xlabel=None, ylabel=None,
              title='title not provided', fignum=None,
              ylims=None, xlims=None,
              logscale=False,
              tikzfile=None, showplot=True):

    lend = len(datalist)
    if markerl is None:
        markerl = ['']*lend
    if leglist is None:
        leglist = [None]*lend

    plt.figure(fignum)
    ax = plt.axes()

    for k, data in enumerate(datalist):
        plt.plot(abscissa, data, markerl[k], label=leglist[k])

    if fit is not None:
        fls = [':', ':']
        for i, cfit in enumerate(fit):
            abspow = []
            for ela in abscissa:
                try:
                    abspow.append((ela/abscissa[0])**(-cfit)*datalist[0][0])
                except TypeError:
                    abspow.append((ela/abscissa[0])**(-cfit)*datalist[0][0][0])
            ax.plot(abscissa, abspow, 'k'+fls[i])

    if logscale:
        ax.set_xscale('log', basex=2)
        ax.set_yscale('log', basey=2)
    if ylims is not None:
        plt.ylim(ylims)
    if xlims is not None:
        plt.xlim(xlims)

    plt.legend()
    plt.grid(which='major')
    _gohome(tikzfile, showplot)
    return


def para_plot(abscissa, datalist, leglist=None, levels=None,
              markerl=None, xlabel=None, ylabel=None,
              title='title not provided', fignum=None,
              ylims=None, xlims=None,
              logscale=None, logscaley=None,
              tikzfile=None, showplot=True,
              colorscheme=None):

    lend = len(datalist)
    if markerl is None:
        markerl = ['']*lend
    if leglist is None:
        leglist = [None]*lend
    # handllist = ['lghdl{0}'.format(x) for x in range(lend)]

    plt.figure(fignum)
    ax = plt.axes()

    leghndll = []
    for k, data in enumerate(datalist):
        labl = leglist[k]
        if labl is None:
            plt.plot(abscissa, data, markerl[k], linewidth=3, label=leglist[k])
        else:
            # hndl = handllist[k]
            hndl, = plt.plot(abscissa, data,
                             markerl[k], linewidth=3, label=leglist[k])
            leghndll.append(hndl)

    if levels is not None:
        for lev in levels:
            ax.plot([abscissa[0], abscissa[-1]], [lev, lev], 'k')

    if logscale is not None:
        ax.set_xscale('log', basex=logscale)
        ax.set_yscale('log', basey=logscale)
    elif logscaley is not None:
        ax.set_yscale('log', basey=logscaley)
    if ylims is not None:
        plt.ylim(ylims)
    if xlims is not None:
        plt.xlim(xlims)

    # plt.legend(handles=leghndll)
    plt.legend()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # plt.grid(which='both')

    _gohome(tikzfile, showplot)

    return


def _gohome(tikzfile=None, showplot=True):
    if tikzfile is not None:
        try:
            from matplotlib2tikz import save as tikz_save
            tikz_save(tikzfile,
                      figureheight='\\figureheight',
                      figurewidth='\\figurewidth')
            print 'you may want to use this command\n\\input{' +\
                tikzfile + '}\n'
        except ImportError:
            print 'matplotlib2tikz need to export tikz filez'

    if showplot:
        plt.show(block=False)
