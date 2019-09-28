# Write a modulethat queries the user for two IP addresses (source and destination) and then
#thesubnet mask of the source. The user will enter all threeinusualdot decimalnotation.
#The programwill then print the mask and the two addresses in binary format(in separate rows and aligned with each other


def main(a_source_ip_address,a_dest_ip_address,a_mask_address):
    """This function convert ip address to ints binary format for Source, Destination and mask
    """

    bin_source_ip = [format(int(no),'08b') for no in a_source_ip_address.split('.')] # IDEA: convert ip address to list of binary number for decimal point.
    bin_dest_ip = [format(int(no),'08b') for no in  a_dest_ip_address.split('.')]
    bin_mask_ip = [format(int(no),'08b') for no in a_mask_address.split('.')]


    print('\nBinary of Source IP addresse', a_source_ip_address , ' is :\t', '.'.join(bin_source_ip))
    print('Binary of Destination addresse', a_dest_ip_address , ' is :\t',  '.'.join(bin_dest_ip))
    print('Binary of Mask addresse', a_mask_address , ' is :\t\t',  '.'.join(bin_mask_ip))

if __name__ == '__main__':
    source_ip_address = input("Enter Source IP addresse:")
    dest_ip_address = input("Enter Destination IP addresse:")
    mask_address = input("Enter Mask  addresse:")
    main(source_ip_address,dest_ip_address,mask_address)
