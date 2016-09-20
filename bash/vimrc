""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> VIMRC <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> UTF8 <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set encoding=utf-8



set nocompatible              " required
filetype off                  " required


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Set the runtime path to include Vundle and initialize <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Plugins <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
Bundle 'Valloric/YouCompleteMe'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'kien/ctrlp.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'nanotech/jellybeans.vim'
Bundle 'ervandew/supertab'                                                      
Bundle 'SirVer/ultisnips'
 

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> All Plugins Above Here <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
call vundle#end()            " required
filetype plugin indent on    " required

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> PEP8 Lines 80 Character <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
au BufWinEnter * let &colorcolumn=join(range(81,999),",")
au BufWinEnter * let &colorcolumn="80,".join(range(400,999),",")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Pretty Stuff Here <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Disable scrollbars 
set guioptions-=r
set guioptions-=R
set guioptions-=l
set guioptions-=L

let python_highlight_all=1
syntax on

set t_Co=256

syntax enable
set background=dark
colorscheme jellybeans

set nu


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> vim-airline settings <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set laststatus=2 " Always display the statusline in all windows
set showtabline=2 " Always display the tabline
set noshowmode " Hide the default mode text
let g:airline_powerline_fonts = 1

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Auto-complete customization <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

let g:ycm_key_list_select_completion = ['<C-n>', '<Down>']                      
let g:ycm_key_list_previous_completion = ['<C-p>', '<Up>']                      
let g:SuperTabDefaultCompletionType = '<C-n>'                                   
                                                                                
" better key bindings for UltiSnipsExpandTrigger                                
let g:UltiSnipsExpandTrigger = "<tab>"                                          
let g:UltiSnipsJumpForwardTrigger = "<tab>"                                     
let g:UltiSnipsJumpBackwardTrigger = "<s-tab>" 


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> python with virtualenv support <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
  project_base_dir = os.environ['VIRTUAL_ENV']
  activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
  execfile(activate_this, dict(__file__=activate_this))
EOF


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Enable folding <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set foldmethod=indent
set foldlevel=99

" Enable folding with the spacebar
nnoremap <space> za

let g:SimpylFold_docstring_preview=1


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> PEP8 Tabs<<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \ set softtabstop=4
    \ set shiftwidth=4
    \ set textwidth=79
    \ set expandtab
    \ set autoindent
    \ set fileformat=unix


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> filetype tabs <<
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
au BufNewFile,BufRead *.js, *.html, *.css
    \ set tabstop=2
    \ set softtabstop=2
    \ set shiftwidth=2


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Whitespace Flagging <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" >> Turn persistent undo on <<
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
try
    set undodir=~/.vim/undo
    set undofile
catch
endtry 
