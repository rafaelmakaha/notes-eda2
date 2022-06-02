type TTreeNode = TreeNode | null

class TreeNode {
  left: TTreeNode = null
  right: TTreeNode = null
  height: number = 1
  constructor(
    public value: number,
  ) { }
}

class Tree {
  public insert(root: TTreeNode | null, key: number): TTreeNode {
    // check if tree is null
    if (root === null) return new TreeNode(key)
    if (key < root.value) root.left = this.insert(root.left, key)
    else root.right = this.insert(root.right, key)

    // update height
    root.height = this.updateHeight(root)

    const bf = this.getBalanceFactor(root)

    if (bf > 1 && key < root.left.value) return this.spinRight(root)
    if (bf < -1 && key > root.right.value) return this.spinLeft(root)
    if (bf > 1 && key > root.left.value) {
      root.left = this.spinLeft(root.left)
      return this.spinRight(root)
    }
    if (bf < -1 && key < root.right.value) {
      root.right = this.spinRight(root.right)
      return this.spinRight(root)
    }

    return root
  }

  public delete(root: TTreeNode, key: number): TTreeNode {
    if (root === null) return root
    if (key < root.value) root.left = this.delete(root.left, key)
    else if (key > root.value) root.right = this.delete(root.right, key)
    else {
      let aux: TTreeNode
      if (root.left === null) {
        aux = root.right
        root = null
        return aux
      }
      else if (root.right === null) {
        aux = root.left
        root = null
        return aux
      }
      aux = this.getSmallestNodeValue(root.right)
      root.value = aux.value
      root.right = this.delete(root.right, aux.value)
    }

    root.height = this.updateHeight(root)

    let bf = this.getBalanceFactor(root)

    if (bf > 1 && this.getBalanceFactor(root.left) >= 0) return this.spinRight(root)
    if (bf < -1 && this.getBalanceFactor(root.right) <=0) return this.spinLeft(root)
    if (bf > 1 && this.getBalanceFactor(root.left) < 0) {
      root.left = this.spinRight(root)
      return this.spinRight(root)
    }
    if (bf < -1 && this.getBalanceFactor(root.right) > 0){
      root.right = this.spinRight(root.right)
      return this.spinLeft(root)
    }

    return root
  }

  public getHeight(root: TTreeNode): number {
    /**
     * Returns tree height.
     */
    if (root === null) return 0
    return root.height
  }

  public spinRight(a: TTreeNode): TTreeNode {
    const b = a.right
    const c = b.left

    b.left = a
    a.right = c

    a.height = this.updateHeight(a)
    b.height = this.updateHeight(b)

    return b
  }

  public spinLeft(a: TTreeNode): TTreeNode {
    const b = a.right
    const c = b.left

    b.left = a
    a.right = c

    a.height = this.updateHeight(a)
    b.height = this.updateHeight(b)

    return b
  }

  public updateHeight(root: TTreeNode): number {
    return 1 + Math.max(this.getHeight(root.left), this.getHeight(root.right))
  }

  public getBalanceFactor(root: TTreeNode): number {
    /**
     * Returns Balance Factor of provided tree.
     * The difference between the depth of right and left sub-trees cannot be more than one. 
     * This difference is called the balance factor.
    */
    if (root === null) return 0
    return this.getHeight(root.left) - this.getHeight(root.right)
  }

  public getSmallestNodeValue(root: TTreeNode): TTreeNode {
    /**
     * Returns the smaller value on the tree
     */
    if (root === null || root.left === null) return root
    return this.getSmallestNodeValue(root.left)
  }

  public printInOrder(root: TTreeNode): void {
    if (root === null) return 
    this.printInOrder(root.left)
    console.log(`${root.value} `)
    this.printInOrder(root.right)
  }
}


// instatiate tree
let avl = new Tree()
let root = null

// const MAX_ARRAY_LENGTH = 10
// const MAX_VALUE = 1000

// const arrayLength = ~~(Math.random() * MAX_ARRAY_LENGTH)
// console.log(arrayLength)

// let values = Array.from(Array(arrayLength)).map(() => ~~(Math.random() * MAX_VALUE))

let values = [6, 8, 0, 7, 9, 1, 3, 4, 2, 5]

let avlTime = []

values.map((value: number) => {
  console.log(`Insert ${value}`)
  root = avl.insert(root, value)
  
  console.log('Print in order: ')
  avl.printInOrder(root)
})
