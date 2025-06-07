import os, argparse, sys, shutil, yaml
def main():
    args = parse_args()
    print_args(args)
    generate_config_directory("test")
    save_args(args, "test")
    # generate_general_config()
    # generate_node_config()

def parse_args(test_args=None):
    """
    Parsing command-line arguments 解析命令行参数
    >>> args = parse_args(['structure.file', '--chunk-size', '2MB', '--total-size', '100MB', '--algorithm', 'testAlgorithm'])
    >>> args.structure
    'structure.file'
    >>> args.chunk_size
    '2MB'
    >>> args.total_size
    '100MB'
    >>> args.algorithm
    'testAlgorithm'
    """

    parser = argparse.ArgumentParser(description="A parser for arguments of configure.py")

    # Add must-chosen arguments 添加必输的命令行参数
    parser.add_argument('structure', help='the web structure file')

    # Add alternative arguments 添加可选的命令行参数
    chunk_group = parser.add_argument_group('Chunk configuration')
    chunk_group.add_argument('--chunk-size', default='1MB', help='size of a single chunk')
    chunk_group.add_argument('--total-size', default='10MB', help='size of the total file')
    
    parser.add_argument('--algorithm', default='defaultTestAlgorithm', help='algorithm')

    # Default: reading from argv except passing in list 不传入参数:默认从argv中获取
    return parser.parse_args(test_args) 

def print_args(args):
    """
    Print the parsed arguments 打印解析后的参数
    >>> args = parse_args(['structure.file', '--chunk-size', '2MB', '--total-size', '100MB', '--algorithm', 'testAlgorithm'])
    >>> print_args(args)
    ------ Arguments ------
    structure: structure.file
    chunk_size: 2MB, total_size: 100MB
    algorithm: testAlgorithm
    <BLANKLINE>
    """

    print('------ Arguments ------')
    print(f"structure: {args.structure}")
    print(f"chunk_size: {args.chunk_size}, total_size: {args.total_size}")
    print(f"algorithm: {args.algorithm}\n")

def generate_config_directory(directory_name : str):
    """
    Ensure the directory exists 确保目录存在
    >>> generate_config_directory('_test_dir_')
    >>> os.path.exists('configure/_test_dir_')
    True
    >>> os.path.exists('configure/_test_dir_/general')
    True
    >>> os.path.exists('configure/_test_dir_/nodes')
    True
    >>> shutil.rmtree('configure/_test_dir_')
    """
    relative_path = 'configure/' + directory_name
    if os.path.exists(relative_path):
        result = input(f"Directory \"{relative_path}\" exists, do you want to rewrite it? (Y/N)\n")
        result = result.upper()
        if (result == "Y" or result == "YES"):
            print(f"Cleaning files in Directory \"{relative_path}\"")

            # equals to "rm -rf {relative_path}"
            shutil.rmtree(relative_path)   
        else:
            print("Execution terminated")
            sys.exit()
    
    os.makedirs(relative_path + '/nodes')
    os.makedirs(relative_path + '/general')

def save_args(args, directory_name : str):
    """
    Saving arguments into args.yaml 保存参数到args.yaml文件
    >>> args = parse_args(['structure.file', '--chunk-size', '2MB', '--total-size', '100MB', '--algorithm', 'testAlgorithm'])
    >>> generate_config_directory('_test_dir_')
    >>> save_args(args, '_test_dir_')
    >>> os.path.exists('configure/_test_dir_/args.yaml')
    True
    >>> with open("configure/_test_dir_/args.yaml", "r") as f :
    ...     actual_data = yaml.safe_load(f)
    ...     actual_data == vars(args)
    True
    >>> shutil.rmtree('configure/_test_dir_')
    """

    relative_path = 'configure/' + directory_name + '/args.yaml'
    with open(relative_path, 'w') as file:
        yaml.dump(vars(args), file, default_flow_style=False)
    print(f"Writing arguments into File \"{relative_path}\"")

def generate_general_config(args, directory_name : str):
    """
    Writing conconfig.ini, preconfig.ini, aggregatorcat.ini, aggregatorput.ini 写入四个通用配置文件
    """


if __name__ == "__main__":
    main()
