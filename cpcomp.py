import sys
import os
import cursed_cpp


template_part1 = """
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <tuple>
#include <limits>

using namespace std;

typedef long long int ll;
typedef long double ld;
typedef double db;


#define loop(a) for (ll __temp_looping_var = 0; __temp_looping_var < a; __temp_looping_var++)
#define repi(a, b) for(ll i = a; i < b; i++)
#define repk(a, b) for(ll k = a; k < b; k++)
#define repj(a, b) for(ll j = a; j < b; j++)


"""


template_part2 = """
int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	solve();

	cout << flush;

	return 0;
}
"""


print('')


args = sys.argv[1:]




comp_flag = False


if '-c' in args:
	comp_flag = True
	args.remove('-c')





if len(args) == 1:

	with open( args[0] , 'r' ) as f:
		with open( f'cpcomp_{args[0]}' , 'w' ) as f2:

			f2.write( template_part1 + cursed_cpp.uncurse( f.read() ) + template_part2 )


	if comp_flag:
		os.system(f'g++ "cpcomp_{args[0]}" -o bin')


elif len(args) == 2:

	with open( args[0] , 'r' ) as f:
		with open( args[1], 'w' ) as f2:

			f2.write( template_part1 + cursed_cpp.uncurse( f.read() ) + template_part2 )


	if comp_flag:
		os.system(f'g++ "{args[1]}" -o bin')


elif len(args) == 3:

	with open( args[0] , 'r' ) as f:
		with open( args[1], 'w' ) as f2:

			f2.write( template_part1 + cursed_cpp.uncurse( f.read() ) + template_part2 )

	
	os.system(f'g++ "{args[1]}" -o {args[2]}')