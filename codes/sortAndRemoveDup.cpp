

/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Sagar Balwani IIIT-H
 _._._._._._._._._._._._._._._._._._._._._.*/

#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include <bitset>
#include <string>
#include <queue>
#include <fstream>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>

using namespace std;

/* General Declarations */
#define SZ(a) int((a).size())
#define all(c) c.begin(),c.end() //all elements of a container
#define rall(c) c.rbegin(),c.rend() 
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traversing a container..works for any type of container
#define present(container, element) (container.find(element) != container.end())    //used for set...return 1 if el is ps 0 otherwise
#define cpresent(container, element) (find(all(container),element) != container.end())  //same as present...but is for vectors

#define INF	        1000000007
#define LL	        long long int
#define INFL	        (LL)1000000007
#define SI(n)		scanf("%lld",&n)
#define SC(c)		scanf("%c",&c)
#define SS(s)		scanf("%s",s)
#define FOR(x,a,b)	for(LL x=a;x<b;x++)
#define REP(i,n)	for(LL i=0;i<n;i++)
#define MP	    	make_pair
#define PB	    	push_back
#define	F	       	first
#define S		second
#define SCAN(v,n)	vector<int> v;REP(i,n){ int j;SI(j);v.PB(j);}
#define PRINT(v,n)	REP(i,n){printf("%lld ",v[i]);}printf("\n");

/* Container's */

#define	VI	       	vector<LL>
#define PLL         	pair<LL,LL>  /* A Single Pair  */
#define VP	    	vector<PLL> /* Vector of Pairs */
#define VS	    	vector<string>
#define VVI		vector<VI>
#define VVS	    	vector<VS>
//Note a & b should both fit in LL
template<class T>inline T GCD(T a,T b){return b?GCD(b,a%b):a;}
template<class T> inline T LCM(T a,T b){if(a<0)return LCM(-a,b);if(b<0)return LCM(a,-b);return a*(b/GCD(a,b));}
template<class T>inline T POW1(T a,T b,T m){long long x=1,y=a;while(b > 0){if(b%2 == 1){x=(x*y);if(x>m) x%=m;}y = (y*y);if(y>m) y%=m;b /= 2;}return x;}
template<class T>inline T INV(T n,T m){return POW1(n,m-2,m);}
template<class T>inline T SUB(T a,T b,T m){return (a%m-b%m+m)%m;}
template<class T>inline T ADD(T a,T b,T m){return (a%m+b%m)%m;}
template<class T>inline T MUL(T a,T b,T m){return (a%m*b%m)%m;}
template<class T>inline T DIV(T a,T b,T m){return (a%m*(INV(b,m))%m)%m;}
vector<int> split(string x, string d)
{
	vector<int> res;
	int prev = 0, found = x.find(d);
	string temp;
	while(found!=std::string::npos)
	{
		temp=x.substr(prev,found-prev);
		res.push_back(atoi(temp.c_str()));
		prev = found+1;
		found = x.find(d, found+1);
	}
	int sz=x.size();
	temp=x.substr(prev,sz-prev);
	res.push_back(atoi(temp.c_str()));
	return res;
}
bool friends[239][239];
vector < vector<int> > vv;
ifstream matin("238graph");
string cliquesDir = "./cliques";
string bestKDir = "./top_cliques";
bool foo(vector<int> a, vector<int> b)
{
	// comparator for sort by size
	return a.size() >  b.size();
}
void printVV(vector<vector<int> > &v,string outputfile)
{
	ofstream outfile(outputfile.c_str());
	REP(i,v.size())
	{
		//printVector(v[i],outputfile);
		outfile << v[i][0];
		FOR(j,1,v[i].size())
		{
			outfile<< " " << v[i][j] ;
		}
		outfile << endl;
	}
}
void sortBySize(string filename)
{
	vv.clear();
	string s;
	vector<int> v;
	ifstream infile(filename.c_str());
	while(getline(infile,s))
	{
		v= split(s," ");
		vv.PB(v);
	}
	sort(all(vv),foo);
}

void AreCliques(vector<vector<int> > &vv)
{
	// requires friends matrix
	REP(i,vv.size())
	{
		REP(j,vv[i].size())
		{
			FOR(k,j+1,vv[i].size())
			{
				if(!friends[vv[i][j]][vv[i][k]])
				{
					cout << " some of it is not a clique\n";  
					return ;
				}
			}
		}
		//printVector(vv[i]);
	}
	cout << "hello everything went fine" << endl; 
}
int intersection(vector<int> &a ,vector<int> & b)
{
	// assumes a and b are sorted
	int l=a.size();
	int m=b.size();
	vector<int> c(l+m);
	return (set_intersection(all(a),all(b),c.begin()) - c.begin());
}
vector<vector<int> > selectBestK(int k, float cmnf,int maxc)
{
	float commonfactor = cmnf;
	vector<vector <int > > res;
	if(vv.size()==0)
	{
		return res;
	}
	int l =vv.size(),ct=0;
	REP(i,l)
	{
		if(vv[i].size() < maxc)
		{
			res.PB(vv[i]);
			break;
		}
	}
	REP(i,l)
	{
		int flag=0;
		//		cout << " fr is "  ;
		if(vv[i].size() > maxc  )
		{
			continue;
		}
		REP(j,res.size())
		{
			float fr = intersection(vv[i],res[j]) *1.0/ vv[i].size()*1.0;
			//			cout << fr  << " " ;
			if(fr  > commonfactor)
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			//			cout << "adding this one\n";
			res.PB(vv[i]);
			ct++;
			if(ct>=k-1)
				break;
		}
	}
	return res;

}
int main()
{
	vector<string> files;
	vector<string> outfiles;
	DIR *dir;
	struct dirent *ent;
	if ((dir = opendir (cliquesDir.c_str())) != NULL) {
		/* print all the files and directories within directory */
		while ((ent = readdir (dir)) != NULL) {
			string s=ent->d_name;
			if(s[0]!='.')
			{
				files.PB(cliquesDir + '/' + s);
				outfiles.PB(bestKDir + '/' + s + ".bestk" );
			//	cout << s << endl;
			}
			//printf ("%s\n", ent->d_name);
		}
		closedir (dir);
	} else {
		/* could not open directory */
		perror ("");
		return EXIT_FAILURE;
	}
		mkdir(bestKDir.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
		cout << "value of k\n" ;
			int k,maxc;
			float cf;
			cin >> k;
			cout << "input common factor\n";
			cin >> cf;
			cout << "max clique size limit\n";
			cin >> maxc;

		REP(i,files.size())
		{
		//	cout << files[i]  << " " << outfiles[i]	 << endl;
			sortBySize(files[i]);
						vector<vector<int> > res=selectBestK(k,cf,maxc);
		printVV(res,outfiles[i]);
		}
	return 0;
}
